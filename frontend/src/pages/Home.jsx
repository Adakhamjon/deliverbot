// import { useEffect } from 'react';
// import { useStore } from '../store/useStore';
// import { getCategories } from '../api/api';
// import { Link } from 'react-router-dom';

// function Home() {
//   const { categories, setCategories } = useStore();

//   useEffect(() => {
//     console.log('Fetching categories...');           
//     getCategories()
//       .then(res => {
//   setCategories(res.data.results || res.data);
// })
//       .catch(err => {
//         console.error('Error:', err);             
//       });
//   }, []);

//   console.log('Render categories:', categories);      

//   return (
//     <div className="home">
//       <h1>🍽️ Oshxona</h1>
      
//       {/* Agar categories bo'sh bo'lsa */}
//       {categories.length === 0 && <p>Yuklanmoqda...</p>}
      
//       <div className="categories">
//         {categories.map(cat => (
//           <Link 
//             key={cat.id} 
//             to={`/menu?category=${cat.id}`}
//             className="category-card"
//           >
//             <h2>{cat.name}</h2>
//           </Link>
//         ))}
//       </div>
      
//       <Link to="/cart" className="cart-link">
//         🛒 Savat ({categories.length})
//       </Link>
//     </div>
//   );
// }

// export default Home;

import { useEffect } from 'react';
import { useStore } from '../store/useStore';
import { getCategories } from '../api/api';
import { Link } from 'react-router-dom';

function Home() {
  const { categories, setCategories } = useStore();

  useEffect(() => {
    getCategories().then(res => setCategories(res.data.results || res.data));
  }, []);

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-primary text-white p-4 shadow-lg">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <span className="text-3xl">🍽️</span>
          <h1 className="text-2xl font-bold">Oshxona</h1>
        </div>
      </header>

      {/* Main */}
      <main className="max-w-4xl mx-auto p-4">
        <h2 className="text-xl font-semibold mb-4 text-gray-700">Kategoriyalar</h2>
        
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {categories.map(cat => (
            <Link 
              key={cat.id} 
              to={`/menu?category=${cat.id}`}
              className="bg-white rounded-xl shadow-md p-6 text-center 
                         hover:shadow-lg hover:scale-105 transition-all
                         border-2 border-transparent hover:border-primary"
            >
              <div className="text-4xl mb-2">
                {cat.name === 'Salatlar' && '🥗'}
                {cat.name === 'Ichimliklar' && '🥤'}
                {cat.name === 'Milliy taomlar' && '🍚'}
                {cat.name === 'Shashlik' && '🍖'}
                {cat.name === 'Fast Food' && '🍔'}
                {cat.name === 'Desertlar' && '🍰'}
              </div>
              <h3 className="font-semibold text-gray-800">{cat.name}</h3>
            </Link>
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

export default Home;