
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Job(db.Model): # is class ma hum apna table create kar rai hian jis ma hum apna data paas karain ga 
    id=db.Column(db.Integer, primary_key=True) # id ka instance banaya hai or is ko primary key bana diya hai, nullable false karn aka mtlb hai ka input must hai us ka begair error aai ga
    job_title=db.Column(db.String(100), nullable=False) # job ka title ka column bana rai hain 
    company_name=db.Column(db.String(100), nullable=False) # comaony name ka column bana rai hain 
    country_name=db.Column(db.String(100), nullable=False) # countrry name ka column bana rai hian 
    job_link=db.Column(db.String(200), nullable=True) # job link ko save karna ka liya colum bana rai hian 
    posted_time=db.Column(db.String(200), nullable=True)

    def to_dict(self): # is function ma hum apna data table ko pass kar rai hian 
        return{
            'id' :self.id,
            'job_title' :self.job_title,
            'company_name' :self.company_name,
            'country_name' :self.country_name,
            'job_link':self.job_link,
            'posted_time':self.posted_time,
        }
