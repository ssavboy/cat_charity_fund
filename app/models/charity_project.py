from sqlalchemy import Column, String, Text

from .base import CharityDonationBase

TEMPLATE_REPR = '{name} {description}'


class CharityProject(CharityDonationBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        template = TEMPLATE_REPR.format(
            name=self.name, description=self.description
        )
        return f'{super().__repr__()} {template}'
