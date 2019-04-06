import filters

def main():
    #Ask what image the user wants to edit
    filename = input("Enter the name of the image file to edit: ")

    #Load the image from the specified filename
    img = filters.load_img(filename)

    #Ask which filter the user wants to use
    filter_choice = input("Which filter would you like: obamicon, brighten, grayscale, or invert? ")

    #Apply chosen filter
    if filter_choice == "obamicon":
        new_img = filters.obamicon(img)

    elif filter_choice == "brighten":
        new_img = filters.brighten(img)

    elif filter_choice == "invert":
        new_img = filters.invert_colors(img)

    elif filter_choice == "grayscale":
        new_img = filters.grayscale(img)

    else:
        print("Sorry, that is not an option.")

    #Save the final filtered Image
    filters.save_img(new_img, "recolored.jpg")

#SETUP CODE
if __name__ == "__main__":
    main()
