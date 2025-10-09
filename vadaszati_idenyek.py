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
    months = ["Márc","Ápr","Máj","Jún","Júl","Aug","Szept","Okt","Nov","Dec","Jan","Feb"]
    # Set "species", "subspecies_colors", "strip_size" based of value of "select"
    match select:
        case 0:
            species = "Gímszarvas"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "borjú":                        (["#8ba02c" if x else "#dddddd" for x in [1,1,0,0,0,0,1,1,1,1,1,1]], None),
                "ünő":                          (["#8ba02c" if x else "#dddddd" for x in [0,0,1,1,1,1,1,1,1,1,1,1]], None),
                "tehén":                        (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]], None),
                "csapos bika":                  (["#a0472c" if x else "#dddddd" for x in [1,0,0,0,0,0,1,1,1,1,1,1]], None),
                "(selejt) bika":                (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,0]], None),
                "érett bika":                   (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,0,0,0,0]], None),
            }
            strip_size = 0.6
            font_size = 20
            picture_size_px = (760, 760)
        case 1:
            species = "Dámszarvas"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "borjú":                        (["#8ba02c" if x else "#dddddd" for x in [1,1,1,0,0,0,0,1,1,1,1,1]], None),
                "ünő":                          (["#8ba02c" if x else "#dddddd" for x in [0,0,0,1,1,1,1,1,1,1,1,1]], None),
                "tehén":                        (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "csapos bika":                  (["#a0472c" if x else "#dddddd" for x in [1,1,0,0,0,0,0,1,1,1,1,1]], None),
                "(selejt) bika":                (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "érett bika":                   (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,0,0,0]], None),
            }
            strip_size = 0.6
            font_size = 20
            picture_size_px = (760, 760)
        case 2:
            species = "Őz"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "gida":                         (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "suta":                         (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "bak":                          (["#a0472c" if x else "#dddddd" for x in [0,0,1,1,1,1,1,1,0,0,0,0,0]], "Ápr"),
            }
            strip_size = 0.4
            font_size = 22
            picture_size_px = (640, 640)
        case 3:
            species = "Muflon"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "bárány":                       (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]], None),
                "jerke":                        (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]], None),
                "juh":                          (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]], None),
                "kos":                          (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
            }
            strip_size = 0.5
            font_size = 22
            picture_size_px = (640, 640)
        case 4:
            species = "Vaddisznó"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "malac (<20kg)":                (["#8ba02c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "süldő (<50kg)":                (["#8ba02c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "koca (>50kg)":                 (["#c02828" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "kan":                          (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
            }
            strip_size = 0.5
            font_size = 22
            picture_size_px = (640, 640)
        case 5:
            species = "Szikaszarvas"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "borjú":                        (["#8ba02c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "ünő":                          (["#8ba02c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "tehén":                        (["#c02828" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "bika":                         (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
            }
            strip_size = 0.5
            font_size = 22
            picture_size_px = (640, 640)
        case 6:
            species = "Apróvadfajok"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "fácán  [2]":                   (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,1]], None),
                "fogoly  [3]":                  (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,0,0]], None),
                "vörös fogoly  [4]":            (["#c02828" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "üregi nyúl":                   (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "mezei nyúl":                   (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,0,0]], None),
            }
            strip_size = 0.6
            font_size = 20
            picture_size_px = (740, 740)
        case 7:
            species = "Apróvadfajok"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "nyári lúd  [5]":               (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,0]], None),
                "vetési lúd  [5]":              (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,0]], None),
                "nagy lilik  [5]":              (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,0]], None),
                "kanadai lúd  [6]":             (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,0]], None),
                "nílusi lúd  [6]":              (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,1,1,1,1,0]], None),
                "örvös galamb":                 (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1,0]], "Aug"),
                "balkáni gerle":                (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1,0]], "Aug"),
                "tőkés réce  [7]":              (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1,0]], "Aug"),
                "szárcsa  [7]":                 (["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,0]], None),
                "erdei szalonka":               (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,0,0,0,0,0,0,0,0]], None),
            }
            strip_size = 0.7
            font_size = 18
            picture_size_px = (820, 820)
        case 8:
            species = "Egyéb apróvadfajok"
            subspecies_colors = {                                                            #3,4,5,6,7,8,9,A,B,C,1,2
                "mosómedve  [8]":               (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "nyestkutya  [8]":              (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "pézsmapocok":                  (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "nyest":                        (["#a0472c" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "aranysakál":                   (["#c02828" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "róka":                         (["#c02828" if x else "#dddddd" for x in [1,1,1,1,1,1,1,1,1,1,1,1]], None),
                "szajkó  [9]":                  (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
                "szarka  [9]":                  (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
                "dolmányos varjú  [9]":         (["#8ba02c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
                "házi görény  [9]":             (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
                "borz  [9]":                    (["#a0472c" if x else "#dddddd" for x in [0,0,0,0,1,1,1,1,1,1,1,1]], None),
            }
            strip_size = 0.7
            font_size = 18
            picture_size_px = (980, 980)
        case _:
            raise ValueError("No species got selected")

    return (months, species, subspecies_colors, strip_size, font_size, picture_size_px)
