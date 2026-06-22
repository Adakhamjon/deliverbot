import { useStore } from '../store/useStore';
import { Link } from 'react-router-dom';

function Cart() {
  const { cart, updateQuantity, removeFromCart, getTotal } = useStore();

  if (cart.length === 0) {
    return (
      <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center">
        <div className="text-6xl mb-4">🛒</div>
        <h1 className="text-2xl font-bold mb-4">Savat bo'sh</h1>
        <Link to="/" className="bg-primary text-white px-6 py-3 rounded-lg">
          Menyuga qaytish
        </Link>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 pb-24">
      {/* Header */}
      <header className="bg-primary text-white p-4 shadow-lg">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <Link to="/" className="text-2xl">←</Link>
          <h1 className="text-xl font-bold">Savat</h1>
          <span></span>
        </div>
      </header>

      {/* Items */}
      <main className="max-w-4xl mx-auto p-4">
        <div className="space-y-4">
          {cart.map(item => (
            <div key={item.id} className="bg-white rounded-xl shadow-md p-4">
              <div className="flex justify-between items-start mb-3">
                <h3 className="font-bold text-lg">{item.name}</h3>
                <button 
                  onClick={() => removeFromCart(item.id)}
                  className="text-danger text-xl"
                >
                  🗑️
                </button>
              </div>
              
              <div className="flex justify-between items-center">
                {/* Miqdor */}
                <div className="flex items-center gap-3">
                  <button 
                    onClick={() => updateQuantity(item.id, item.quantity - 1)}
                    className="w-10 h-10 bg-gray-200 rounded-lg text-xl"
                  >
                    -
                  </button>
                  <span className="text-xl font-semibold">{item.quantity}</span>
                  <button 
                    onClick={() => updateQuantity(item.id, item.quantity + 1)}
                    className="w-10 h-10 bg-gray-200 rounded-lg text-xl"
                  >
                    +
                  </button>
                </div>
                
                {/* Narx */}
                <p className="text-primary font-bold text-xl">
                  {(item.price * item.quantity).toLocaleString()} so'm
                </p>
              </div>
            </div>
          ))}
        </div>
      </main>

      {/* Footer */}
      <div className="fixed bottom-0 left-0 right-0 bg-white shadow-lg p-4">
        <div className="max-w-4xl mx-auto flex justify-between items-center">
          <div>
            <p className="text-gray-600">Jami:</p>
            <p className="text-2xl font-bold text-primary">
              {getTotal().toLocaleString()} so'm
            </p>
          </div>
          <Link 
            to="/checkout"
            className="bg-secondary text-white px-8 py-4 rounded-xl 
                       text-lg font-semibold hover:scale-105 transition-transform"
          >
            Buyurtma berish →
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Cart;