from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


def donation_or_close(obj):
    obj.invested_amount = obj.full_amount
    obj.fully_invested = True
    obj.close_date = datetime.now()


async def investing(
    session: AsyncSession
):
    projects = await session.execute(
        select(CharityProject).where(
            ~CharityProject.fully_invested
        ).order_by(CharityProject.create_date)
    )
    for project in projects.scalars().all():
        donations = await session.execute(
            select(Donation).where(
                ~Donation.fully_invested
            ).order_by(Donation.create_date)
        )
        for donation in donations.scalars().all():
            project_amount = (
                project.full_amount - project.invested_amount
            )
            donation_amount = (
                donation.full_amount - donation.invested_amount
            )
            if project_amount > donation_amount:
                project.invested_amount += donation_amount
                donation_or_close(donation)
            elif project_amount < donation_amount:
                donation.invested_amount += project_amount
                donation_or_close(project)
            else:
                donation_or_close(project)
                donation_or_close(donation)
            session.add(project)
            session.add(donation)
            if project.fully_invested:
                break
    await session.commit()
