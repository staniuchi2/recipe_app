import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Recipes from './Recipes';
import RecipeDetail from './RecipeDetail';
import Base from "./base";
import AddRecipes from './AddRecipe';

function App() {
    return (
        <div className="App">
            <Routes>
                <Route path="/" element={<Base><Recipes /></Base>} />
                <Route path="/recipes/:recipeId" element={<Base><RecipeDetail /></Base>} />
                <Route path="/add_recipes" element={<Base><AddRecipes /></Base>} />
            </Routes>
        </div>
    );
}

export default App;
