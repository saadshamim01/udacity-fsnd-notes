@app.route('/venues')
@app.route('/venues')
def venues():
    unique_city_states = Venue.query.distinct(Venue.city, Venue.state).all()
    data = [ucs.filter_on_city_state for ucs in unique_city_states]
    print(data)

    return render_template('pages/venues.html', areas=data)


@app.route('/venues/search', methods=['POST'])
def search_venues():
    search_term = request.form.get('search_term', None)
    venues = Venue.query.filter(
        Venue.name.ilike("%{}%".format(search_term))).all()
    count_venues = len(venues)
    response = {
        "count": count_venues,
        "data": [v.serialize for v in venues]
    }
    return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))
