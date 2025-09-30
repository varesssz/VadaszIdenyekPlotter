def ideny(
    select: int,
):
    """Return the seasons of a species (or group of species) for a single figure.

    Args:
        select (int): A number form 0 to 6 to select a species (or group of species).

    Raises:
        ValueError: Raise error in case of "select" is out of range.

    Returns:
        _type_: Tuple of (months, species, subspecies_colors, strip_size) in that order.
    """
    # List of the months starting with the start of the hunting year
    months = ["Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb"]
    # Set "species", "subspecies_colors", "strip_size" based of value of "select"
    match select:
        case 0:
            species = "Gímszarvas"
            subspecies_colors = {                                                        #3,4,5,6,7,8,9,A,B,C,1,2
                "ünő":                      (["#8ba02c" if x else "#dddddd" for x in [0,0,1,1,1,1,1,1,1,1,1,1]], None),
                "borjú":                    (["#8ba02c" if x else "#dddddd" for x in [1,1,0,0,0,0,1,1,1,1,1,1]], None),
                "tehén":                    (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]], None),
                "csapos bika":              (["#a0472c" if x else "#dddddd" for x in [1,0,0,0,0,0,1,1,1,1,1,1]], None),
                "selejt bika":              (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,0]], None),
                "érett bika":               (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,0,0,0,0]], None),
            }
            strip_size = 0.6
        case 1:
            species = "Dámszarvas"
            subspecies_colors = {                                                        #3,4,5,6,7,8,9,A,B,C,1,2
                "ünő":                      (["#8ba02c" if x else "#dddddd" for x in [0,0,0,1,1,1,1,1,1,1,1,1]], None),
                "borjú":                    (["#8ba02c" if x else "#dddddd" for x in [1,1,1,0,0,0,0,1,1,1,1,1]], None),
                "tehén":                    (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "csapos bika":              (["#a0472c" if x else "#dddddd" for x in [1,1,0,0,0,0,0,1,1,1,1,1]], None),
                "selejt bika":              (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "érett bika":               (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,0,0,0]], None),
            }
            strip_size = 0.6
        case 2:
            species = "Őz"
            subspecies_colors = {                                                         #3,4,5,6,7,8,9,A,B,C,1,2
                "gida":                     (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "suta":                     (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "bak":                      (["#a0472c" if x else "#dddddd" for x in [0,0,1,1,1,1,1,1,0,0,0,0,0]], "Apr"),
            }
            strip_size = 0.4
        case 3:
            species = "Muflon"
            subspecies_colors = {                                                        #3,4,5,6,7,8,9,A,B,C,1,2
                "bárány":                   (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]], None),
                "jerke":                    (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]], None),
                "juh":                      (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]], None),
                "kos":                      (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
            }
            strip_size = 0.5
        case 4:
            species = "Apróvadfajok (nyulak és tyúkalakúak)"
            subspecies_colors = {                                                        #3,4,5,6,7,8,9,A,B,C,1,2
                "vörös fogoly":             (["#c02828" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "fogoly":                   (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,0,0]], None),
                "fácán tyúk":               (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "üregi nyúl":               (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "mezei nyúl":               (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,0,0]], None),
            }
            strip_size = 0.6
        case 5:
            species = "Apróvadfajok (lúd- és galambalakúak)"
            subspecies_colors = {                                                        #3,4,5,6,7,8,9,A,B,C,1,2
                "örvös galamb":             (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1,0]], "Aug"),
                "balkáni gerle":            (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1,0]], "Aug"),
                "erdei szalonka":           (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,0,0,0,0,0]], None),
                "szárcsa":                  (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,0]], None),
                "tőkés réce":               (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1,0]], "Aug"),
                "kanadai- és nílusi lúd":   (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,0]], None),
                "nagy lilik":               (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,0]], None),
                "nyári- és vetési lúd":     (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,0]], None),
            }
            strip_size = 0.7
        case 6:
            species = "Egyéb apróvadfajok"
            subspecies_colors = {                                                        #3,4,5,6,7,8,9,A,B,C,1,2
                "mosómedve":                (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "nyestkutya":               (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "pézsmapocok":              (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "nyest":                    (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "aranysakál":               (["#c02828" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "róka":                     (["#c02828" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "szajkó":                   (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
                "szarka":                   (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
                "dolmányos varjú":          (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
                "házi görény":              (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
                "borz":                     (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
            }
            strip_size = 0.7
        case _:
            raise ValueError("No species got selected")
        
        #TODO fajonkénti megjegyzések hozzáadása az ábrához (pl. fácántyúk csak vadászati célú kibocsátása esetén vadászható)

    return (months, species, subspecies_colors, strip_size)
