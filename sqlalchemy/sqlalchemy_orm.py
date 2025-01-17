from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

url = "mysql+pymysql://root:123456@192.168.99.100:3306/sqlalchemy?charset=utf8"
engine = create_engine(
    url,
    echo=True,
    pool_size=8,
    pool_recycle=60*30
)
Base = declarative_base(engine)


class User(Base):  
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True) 
    name = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User',
            backref=backref('course', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Course: {}>'.format(self.name)


if __name__ == '__main__':
    # 使用声明基类的 metadata 对象的 create_all 方法创建数据表：
    Base.metadata.create_all()
