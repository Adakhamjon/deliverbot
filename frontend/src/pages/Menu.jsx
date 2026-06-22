// import { useEffect, useState } from 'react';
// import { useSearchParams } from 'react-router-dom';
// import { useStore } from '../store/useStore';
// import { getMenuItems } from '../api/api';

// function Menu() {
//   const [searchParams] = useSearchParams();
//   const categoryId = searchParams.get('category');
  
//   const { menuItems, setMenuItems, addToCart } = useStore();

//   useEffect(() => {
//     getMenuItems(categoryId).then(res => setMenuItems(res.data.results || res.data));
//   }, [categoryId]);

//   return (
//     <div className="menu">
//       <h1>Menyu</h1>
//       <div className="menu-items">
//         {menuItems.map(item => (
//           <div key={item.id} className="menu-item">
//             <h3>{item.name}</h3>
//             <p>{item.price.toLocaleString()} so'm</p>
//             <button onClick={() => addToCart(item)}>
//               Savatga qo'shish
//             </button>
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// }

// export default Menu;

import { useEffect, useState } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { useStore } from '../store/useStore';
import { getMenuItems } from '../api/api';

function Menu() {
  const [searchParams] = useSearchParams();
  const categoryId = searchParams.get('category');
  
  const { menuItems, setMenuItems, addToCart } = useStore();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    getMenuItems(categoryId).then(res => {
      setMenuItems(res.data.results || res.data);
      setLoading(false);
    });
  }, [categoryId]);

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-2xl">Yuklanmoqda...</div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-50 pb-20">
      {/* Header */}
      <header className="bg-primary text-white p-4 shadow-lg">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <Link to="/" className="text-2xl">←</Link>
          <h1 className="text-xl font-bold">Menyu</h1>
          <span></span>
        </div>
      </header>

      {/* Items */}
      <main className="max-w-4xl mx-auto p-4">
        <div className="space-y-4">
          {menuItems.map(item => (
            <div key={item.id} 
                 className="bg-white rounded-xl shadow-md p-4 flex items-center gap-4">
              {/* Rasm joyi */}
              <div className="w-20 h-20 bg-gray-200 rounded-lg flex items-center justify-center text-3xl">
                🍽️
              </div>
              
              {/* Ma'lumot */}
              <div className="flex-1">
                <h3 className="font-bold text-lg">{item.name}</h3>
                <p className="text-primary font-semibold text-xl">
                  {parseFloat(item.price).toLocaleString()} so'm
                </p>
              </div>
              
              {/* Tugma */}
              <button 
                onClick={() => addToCart(item)}
                className="bg-primary text-white px-6 py-3 rounded-lg
                           hover:bg-green-600 active:scale-95 transition-all"
              >
                +
              </button>
            </div>
          ))}
        </div>
      </main>

      {/* Footer */}
      <Link 
        to="/cart" 
        className="fixed bottom-6 right-6 bg-secondary text-white 
                   p-4 rounded-full shadow-lg hover:scale-110 transition-transform"
      >
        🛒 Savat
      </Link>
    </div>
  );
}

export default Menu;