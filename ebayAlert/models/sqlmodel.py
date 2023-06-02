from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from ebayAlert import create_logger
from ebayAlert.db.db import Base, engine

log = create_logger(__name__)


class EbayPost(Base):
    __tablename__ = "ebay_post"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(String)
    post_id = Column(Integer)
    link_id = Column(Integer)
    date = Column(DateTime(timezone=True), server_default=func.now())


class EbayLink(Base):
    __tablename__ = "ebay_link"

    id = Column(Integer, primary_key=True)
    status = Column(Integer)
    search_type = Column(String)
    search_string = Column(String)
    price_low = Column(Integer)
    price_high = Column(Integer)
    price_target = Column(Integer)
    price_info = Column(String)
    zipcodes = Column(String)
    chat_id = Column(Integer)


Base.metadata.create_all(engine)
