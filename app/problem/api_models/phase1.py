from sqlalchemy import Column, Integer, String, Float, Boolean
from .base import ProblemBase, Base


class NewProblem(Base):
    """help interact with a table in PostgreSQL server"""

    __tablename__ = "Data"
    id = Column(Integer, primary_key=True, index=True)
    # request_id =


class Prob1Table(ProblemBase):
    __tablename__ = "1.1.FraudDetection"

    job = Column(String)
    category = Column(String)
    amt = Column(Float)
    zip = Column(Integer)
    lat = Column(Float)
    long = Column(Float)
    city_pop = Column(Integer)
    merch_lat = Column(Float)
    merch_long = Column(Float)
    age = Column(Float)
    hour = Column(Integer)
    day = Column(Integer)
    month = Column(Integer)
    is_fraud = Column(Boolean)
    trans_freq = Column(Float)
    recent_trans_freq = Column(Float)
    time_since_last = Column(Float)


class Prob2Table(ProblemBase):
    __tablename__ = "1.2.SalaryPrediction"

    work_year = Column(Integer)
    experience_level = Column(String)
    employment_type = Column(String)
    job_title = Column(String)
    salary = Column(Integer)
    salary_currency = Column(String)
    label = Column(Integer)
    employee_residence = Column(String)
    remote_ratio = Column(Float)
    company_location = Column(String)
    company_size = Column(String)
