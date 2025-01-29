from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data from Excel
df = pd.DataFrame({
    'State/Region': [
        'Jammu & Kashmir', 'Ladakh', 'Himachal Pradesh', 'Punjab', 'Haryana',
        'Uttar Pradesh', 'Rajasthan', 'Uttarakhand', 'Gujarat', 'Maharashtra', 
        'Goa', 'West Bengal', 'Odisha', 'Bihar', 'Jharkhand', 'Madhya Pradesh',
        'Chhattisgarh', 'Tamil Nadu', 'Kerala', 'Karnataka', 'Andhra Pradesh',
        'Telangana', 'Assam', 'Meghalaya', 'Arunachal Pradesh', 'Nagaland', 
        'Manipur', 'Mizoram', 'Tripura', 'Sikkim'
    ],
    'Region/Capital/City': [
        'Srinagar', 'Leh', 'Shimla', 'Amritsar', 'Chandigarh', 'Lucknow',
        'Jaipur', 'Dehradun', 'Ahmedabad', 'Mumbai', 'Panaji', 'Kolkata',
        'Bhubaneswar', 'Patna', 'Ranchi', 'Bhopal', 'Raipur', 'Chennai',
        'Thiruvananthapuram', 'Bengaluru', 'Amaravati', 'Hyderabad', 
        'Guwahati', 'Shillong', 'Itanagar', 'Kohima', 'Imphal', 'Aizawl',
        'Agartala', 'Gangtok'
    ],
    'Music/Song Type': [
        'Sufi music, Chakri, Ladakhi songs', 'Folk songs, Monastic chants',
        'Naati, Jhoori, Laman', 'Bhangra, Giddha, Sufi Qawwalis, Punjabi folk songs',
        'Ragini, Seasonal folk songs (Teej, Holi)', 
        'Thumri, Kajri, Chaiti, Bhajans, Qawwalis',
        'Manganiyar and Langa songs, Bhajans, Rajasthani folk',
        'Garhwali and Kumaoni folk songs, Jagar',
        'Garba, Dandiya Raas, Bhajans', 
        'Lavani, Abhangas, Powada, Marathi folk songs', 
        'Konkani folk, Mando, Portuguese fado',
        'Rabindra Sangeet, Baul, Nazrul Geeti, Shyama Sangeet',
        'Odissi classical, Kalinga Giti, Pala, Daskathia',
        'Bhojpuri folk songs (Sohar, Chhath), Birha', 
        'Tribal music, Jhumar, Sohrai', 
        'Alha ballads, Baiga tribal music', 
        'Pandavani, Karma songs, Tribal music',
        'Carnatic music, Villupattu, Tamil film songs',
        'Sopana Sangeetham, Kathakali music, Mappilappattu',
        'Carnatic music, Sugama Sangeetha, Janapada Geethe', 
        'Burrakatha, Jangam Katha, Carnatic music',
        'Carnatic music, Folk songs, Janapada Paatalu',
        'Bihu songs, Goalparia Lokgeet, Zikir', 
        'Khasi folk songs, Christian hymns',
        'Tribal songs, Buddhist chants', 
        'Naga folk songs (war songs, work songs)', 
        'Manipuri classical, Lai Haraoba songs',
        'Mizo folk songs, Christian hymns',
        'Kokborok folk songs, Devotional music', 
        'Bhutia and Lepcha folk songs, Monastic chants'
    ],
    'Latitude': [
        34.0837, 34.1526, 31.1048, 31.634, 30.7333, 26.8467, 26.9124,
        30.3165, 23.0225, 19.076, 15.4909, 22.5726, 20.2961, 25.5941,
        23.3441, 23.2599, 21.2514, 13.0827, 8.5241, 12.9716, 16.5735,
        17.385, 26.1445, 25.5788, 27.0844, 25.6751, 24.817, 23.7271,
        23.8315, 27.3389
    ],
    'Longitude': [
        74.7973, 77.5771, 77.1734, 74.8723, 76.7794, 80.9462, 75.7873,
        78.0322, 72.5714, 72.8777, 73.8278, 88.3639, 85.8245, 85.1376,
        85.3096, 77.4126, 81.6296, 80.2707, 76.9366, 77.5946, 80.3587,
        78.4867, 91.7362, 91.8933, 93.6053, 94.1077, 93.9368, 92.7176,
        91.2868, 88.6065
    ]
})

@app.route('/')
def index():
    # Convert data to a format suitable for the frontend
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

@app.route('/search', methods=['GET'])
def search_song():
    song = request.args.get('song', '')
    # Redirect to YouTube search results for the song
    youtube_url = f"https://www.youtube.com/results?search_query={song}"
    return f"<script>window.open('{youtube_url}', '_blank');</script>"

if __name__ == '__main__':
    app.run(debug=True)
