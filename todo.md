# Connect 4 Game for CS Project

## Utilities to use:-

- PyGame
- Numpy
- Keyboard
- Mouse
- Playsound / OS

## GUI:-

- Game start screen
- Game pause screen
- Game end screen
- Setting menu
- Game pre-initialisation screen
- Main Game Screen

### Main Game Screen

#### Theme Original

- Connect 4 Grid - Blue
- Background - light live gradient
- Red & yellow colour to represent the 2 players

#### Theme Dark

- Connect 4 Grid - dark greyish blue
- Background - dark live gradient
- Blue & white colour to represent the 2 players

#### Theme Colourblind (Optional)

- Connect 4 Grid - warm dark blue
- Background - light live gradient (Only Tan and Turquoise)
- Blue & orangish yellow colour to represent the 2 players

### Settings Menu

- Theme changer
- Music Toggle
- Sound Toggle

## Audio:-

- Game start
- Game pause
- Dropping pieces
- Game over/win
- Background music

## Functionality:-

- Arrow keys and WASD keys
- Mouse
- Drop piece
- Checking win

## Advanced Features (Optional):-

- Basic AI
- Physics of droppping pieces
- Easter Egg

## Check Win Function:-

### Straight (Single column)

- Check downwards
- Min row: 0 and Max row: 2
- incrementing row

### Right (Single row)

- Check right
- Min column: 0 and Max column: 3
- incrementing column

### Left (Single row)

- Check left
- Min column: 3 and Max column: 6
- decrementing column

### Diagonals

#### TL to BR

- By incrementing col and row
- min column: 0 and max column: 3
- min row: 0 and max row: 2

#### BL to TR

- By incrementing col and decrementing row
- min column: 0 and max column: 3
- min row: 3 and max row: 5

#### TR to BL

- By decrementing col and incrementing row
- min column: 3 and max column: 6
- min row: 0 and max row: 2

#### BR to TL

- By decrementing col and row
- min column: 3 and max column: 6
- min row: 3 and max row: 5
