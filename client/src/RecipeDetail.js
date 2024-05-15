import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Card from '@mui/material/Card';


function RecipeDetail() {
  const { recipeId } = useParams(); // This hooks allow you to access the route parameters
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5000/api/recipes/${recipeId}`) // Adjust this URL to where your API is hosted
      .then(response => response.json())
      .then(data => setRecipe(data))
      .catch(error => console.error('Error loading recipe:', error));
  }, [recipeId]); // This effect runs when recipeId changes



  if (!recipe) {
    return <div>Loading...</div>;
  }

  const cardStyle = {
    position: 'fixed',
    top: '10%',
    left: '50%',
    transform: 'translate(-50%, -10%)',
    display: 'flex',
    backgroundColor: 'black',
    variant: 'outlined',
    outlineColor: 'white',
    outlineStyle: "solid",
    outlineWidth: 1,
    color: 'white',
    alignItems: 'center',
    justifyContent: 'center',
    width: '80%'
  };

  return (
    <Card style={cardStyle}>
      <div>
        <h1>{recipe.recipe_id}</h1>
        <p>{recipe.recipe_name}</p>
        {/* Render other recipe details as needed */}
      </div>
    </Card>
    
  );
}

export default RecipeDetail;
