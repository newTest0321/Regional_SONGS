# Indian Regional Songs Map

Explore the rich and diverse musical heritage of India with an interactive map that showcases the various regional songs, their origins, and styles across the country.

## Project Overview

This project provides an engaging way to discover India's musical traditions by mapping various regions, their unique song types, and culture. Users can interact with the map to explore the music styles of each state/region and access related videos or songs on YouTube.

## Features

- **Interactive Map**: Displays the Indian map with markers for each state/region.
- **Custom Popups**: Click on a region to view its musical styles and a button to search songs on YouTube.
- **Search Functionality**: Search for any song directly from the app.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used

### Frontend
- **HTML/CSS**: For structure and styling.
- **JavaScript**: For interactive map elements.
- **Leaflet.js**: To render the map and manage markers.

### Backend
- **Python (Flask)**: Handles server-side logic.
- **Pandas**: For data manipulation.

### Dataset
The dataset includes:
- State/Region names
- Popular music/song types
- Geographic coordinates (latitude and longitude)

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/map_song.git
   ```
2. Navigate to the project directory:
   ```bash
   cd map_song
   ```
3. Install required Python libraries:
   ```bash
   pip install flask pandas
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Folder Structure

```
map_song/
|-- app.py                  # Flask backend
|-- templates/
|   |-- index.html          # Frontend template
|-- static/
|   |-- css/                # CSS files
|   |-- js/                 # JavaScript files
|   |-- images/             # Images and icons
```

## Screenshots

### Home Page
![Home Page Screenshot](screenshot-home.png)

### Interactive Map
![Map Screenshot](screenshot-map.png)

## Future Enhancements

- Add audio previews of regional songs.
- Support for multiple languages.
- Allow users to contribute new song types and data.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Leaflet.js](https://leafletjs.com/) for the interactive map.
- [Flask](https://flask.palletsprojects.com/) for the backend framework.
- Indian music culture for inspiring this project.

---

**Made with ❤️ by [Your Name](https://github.com/your-username)**
