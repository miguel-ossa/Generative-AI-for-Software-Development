
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
from graphviz import Digraph
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_date = Column(DateTime)
    status = Column(String, nullable=False)
    user = relationship('User', back_populates='orders')

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    order = relationship('Order', back_populates='items')
    product = relationship('Product')

User.orders = relationship('Order', order_by=Order.id, back_populates='user')
Order.items = relationship('OrderItem', order_by=OrderItem.id, back_populates='order')

def delete_users():
    # Borrar usuarios existentes
    session.query(User).delete()
    session.commit()

def create_user(session, name, email, password_hash):
    # Comprobar si el email ya existe
    if session.query(User).filter_by(email=email).first() is not None:
        raise ValueError("El email ya está registrado.")

    current_time = datetime.now(timezone.utc)  # Obtener la fecha y hora actuales en UTC
    new_user = User(name=name, email=email, password_hash=password_hash, created_at=current_time)
    session.add(new_user)
    session.commit()
    print(f"Usuario {name} añadido con éxito a las {current_time}.")

def list_users(session):
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Created At: {user.created_at}")

def update_user_email(session, user_id, new_email):
    # Verificar si el nuevo email ya existe
    if session.query(User).filter_by(email=new_email).first() is not None:
        raise ValueError("El nuevo email ya está registrado.")

    # Obtener el usuario por ID
    user = session.query(User).filter_by(id=user_id).first()
    if user is None:
        raise ValueError("Usuario no encontrado.")

    # Actualizar el email
    user.email = new_email
    session.commit()
    print(f"Email del usuario {user.name} actualizado a {new_email}.")

def create_product(session, name, description, price, stock):
    new_product = Product(name=name, description=description, price=price, stock=stock, created_at=datetime.now(timezone.utc))
    session.add(new_product)
    session.commit()
    print(f"Producto {name} añadido con éxito.")

def create_order(session, user_id, status, items):
    order = Order(user_id=user_id, order_date=datetime.now(timezone.utc), status=status)
    session.add(order)
    session.commit()

    for item in items:
        order_item = OrderItem(order_id=order.id, product_id=item['product_id'], quantity=item['quantity'], price=item['price'])
        session.add(order_item)

    session.commit()
    print(f"Orden para el usuario {user_id} creada con éxito.")

def list_orders(session, user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("Usuario no encontrado.")
        return

    print(f"Pedidos para {user.name}:")
    orders = session.query(Order).filter_by(user_id=user_id).all()
    for order in orders:
        print(f"Orden ID: {order.id}, Fecha: {order.order_date}, Estado: {order.status}")
        for item in order.items:
            product = session.query(Product).filter_by(id=item.product_id).first()
            print(f"  Producto: {product.name}, Cantidad: {item.quantity}, Precio: {item.price}")
    print("\n")

def create_er_diagram():
    dot = Digraph(comment='E-Commerce ER Diagram')

    dot.node('User', 'User\nid, name, email, password_hash, created_at')
    dot.node('Product', 'Product\nid, name, description, price, stock, created_at')
    dot.node('Order', 'Order\nid, user_id, order_date, status')
    dot.node('OrderItem', 'OrderItem\nid, order_id, product_id, quantity, price')

    dot.edge('User', 'Order')
    dot.edge('Order', 'OrderItem')
    dot.edge('OrderItem', 'Product')

    dot.render('er_diagram', format='png')
    print('ER diagram generated as er_diagram.png')

if __name__ == "__main__":
    engine = create_engine('sqlite:///ecommerce.db')
    Base.metadata.create_all(engine)
    session = Session(engine)

    delete_users()
    # Añadir un nuevo usuario
    try:
        create_user(session, 'Alice', 'alice@example.com', 'hashedpassword1')
        create_user(session, 'Bob', 'bob@example.com', 'hashedpassword2')
    except ValueError as e:
        print(e)

    # Listar usuarios existentes
    list_users(session)

    try:
        update_user_email(session, user_id=1, new_email='newalice@example.com')
    except ValueError as e:
        print(e)

    list_users(session)

    # Crear productos
    create_product(session, 'Laptop', 'High performance laptop', 1500.00, 10)
    create_product(session, 'Mouse', 'Wireless mouse', 25.00, 50)

    # Obtener IDs de productos
    laptop = session.query(Product).filter_by(name='Laptop').first()
    mouse = session.query(Product).filter_by(name='Mouse').first()

    # Crear órdenes para Alice
    create_order(session, user_id=1, status='completed', items=[
        {'product_id': laptop.id, 'quantity': 1, 'price': laptop.price},
        {'product_id': mouse.id, 'quantity': 2, 'price': mouse.price}
    ])

    # Crear órdenes para Bob
    create_order(session, user_id=2, status='pending', items=[
        {'product_id': mouse.id, 'quantity': 3, 'price': mouse.price}
    ])

    # Listar órdenes para Alice
    list_orders(session, user_id=1)

    # Listar órdenes para Bob
    list_orders(session, user_id=2)

    session.close()

    #create_er_diagram()
