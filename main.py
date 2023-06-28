import json

template_file = "template.tpl.ckd"
output_file = "songdesc.tpl.ckd"

def replace_placeholders(template):
    codename = input("Enter the codename: ")
    jdversion = int(input("Enter the JD version: "))
    artist = input("Enter the artist: ")
    songname = input("Enter the song name: ")
    credits = input("Enter the credits: ")
    codename_undersquare = codename.lower()
    num_coach = int(input("Enter the number of coaches (1-4): "))
    dif_normal = int(input("Enter the normal difficulty (1-4): "))
    dif_sweat = int(input("Enter the sweat difficulty (1-3): "))

    # Replace placeholders with user input
    replaced_template = template.replace("{codename}", codename)
    replaced_template = replaced_template.replace("{jdversion}", str(jdversion))
    replaced_template = replaced_template.replace("{artist}", artist)
    replaced_template = replaced_template.replace("{songname}", songname)
    replaced_template = replaced_template.replace("{credits}", credits)
    replaced_template = replaced_template.replace("{codename_undersquare}", codename_undersquare)
    replaced_template = replaced_template.replace("{num_coach}", str(num_coach))
    replaced_template = replaced_template.replace("{dif_normal}", str(dif_normal))
    replaced_template = replaced_template.replace("{dif_sweat}", str(dif_sweat))

    return replaced_template

def update_songdesc_template(template_file, output_file):
    with open(template_file, "r") as file:
        template = file.read()

    updated_template = replace_placeholders(template)

    with open(output_file, "w") as file:
        file.write(updated_template)

    print(f"Updated template saved to {output_file}")

# Run the script
update_songdesc_template(template_file, output_file)
