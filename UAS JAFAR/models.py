from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Motor(Base):
    __tablename__ = 'data'
    id_motor: Mapped[str] = mapped_column(primary_key=True)
    harga: Mapped[int] = mapped_column()
    teknologi: Mapped[int] = mapped_column()
    kecepatan: Mapped[int] = mapped_column()
    kapasitas: Mapped[int] = mapped_column()
    desain: Mapped[int] = mapped_column()  
    
    def __repr__(self) -> str:
        return f"data(id_motor={self.id_motor!r}, harga={self.harga!r})"
