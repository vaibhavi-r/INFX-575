# Case 1
if "coordinates" in tweet:
    ctr1 += 1
    d = {"case": 1, "tweet_index": i}

    geom = tweet["coordinates"]

    if geom is not None and "coordinates" in geom:
        coords = geom["coordinates"]
        long = coords[0]
        lat = coords[1]
        valid_ctr1 += 1
        d["long"] = long
        d["lat"] = lat

    if geom is not None and "type" in geom:
        d["type"] = geom["type"]

    case1.append(d)

# Case 2 :
if "place" in tweet:
    ctr2 += 1
    place = tweet["place"]
    d = {"case": 3, "tweet_index": i}

    if place is not None:
        valid_ctr2 += 1
        #            if "bounding_box" in place:
        if "country" in place:
            d["country"] = place["country"]

        if "country_code" in place:
            d["country_code"] = place["country_code"]

        if "full_name" in place:
            d["full_name"] = place["full_name"]

        if "name" in place:
            d["name"] = place["name"]

        if "place_type" in place:
            d["place_type"] = place["place_type"]

        if "bounding_box" in place:
            bb = place["bounding_box"]
            if "type" in bb:
                if type == "Polygon":
                    if "coordinates" in bb:
                        coords = bb["coordinates"]
                        d["coordinates"] = coords
                        #                            long = bb[0][0][0]
                        #                            lat = bb[0][0][1]
    case2.append(d)


