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

  var recipe_info = recipe['recipe']
  var ingredients_info = recipe['ingredients']

  
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

  const getIngredientsList = ingredients_info => {
    let list = [];
    for (let i=0 ; i < ingredients_info.length; i++ ){
      const item = ingredients_info[i];
      list.push(<li key={item.ingredient_id}>{item.ingredient_name}  {item.amount}  {item.unit}</li>)
    }
    return list
  }

  const data = recipe_info.recipe_image

  return (
    <Card style={cardStyle}>

      <div>
        <img src={'data:image/jpeg;base64,${data}'} />
        <h1>{recipe_info.recipe_name}</h1>
        <p>{recipe_info.recipe_description}</p>
        <h2>Ingredients</h2>
        <ul>{getIngredientsList(ingredients_info)}</ul>
        <h2>Method</h2>
        <p>{recipe_info.recipe_steps}</p>
        
        {/* Render other recipe details as needed */}
      </div>
    </Card>
    
  );
}

export default RecipeDetail;
