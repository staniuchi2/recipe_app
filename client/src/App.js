import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Recipes from './Recipes';
import RecipeDetail from './RecipeDetail';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Recipes />} />
        <Route path="/recipes/:recipeId" element={<RecipeDetail />} />
      </Routes>
    </div>
  );
}

export default App;
