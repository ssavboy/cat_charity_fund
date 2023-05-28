from sqlalchemy import Column, ForeignKey, Integer, Text

from .base import CharityDonationBase

TEMPLATE_REPR = '{user} {comment}'


class Donation(CharityDonationBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        template = TEMPLATE_REPR.format(
            user=self.user_id, comment=self.comment
        )
        return f'{super().__repr__()} {template}'
