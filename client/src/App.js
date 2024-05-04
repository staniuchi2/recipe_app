import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Recipes from './Recipes';
import RecipeDetail from './RecipeDetail';
import Base from "./base";

function App() {
    return (
        <div className="App">
            <Routes>
                <Route path="/" element={<Base><Recipes /></Base>} />
                <Route path="/recipes/:recipeId" element={<Base><RecipeDetail /></Base>} />
            </Routes>
        </div>
    );
}

export default App;
