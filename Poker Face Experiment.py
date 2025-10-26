from psychopy import core, visual, event, data, gui
import pandas as pd
import os

# Get participant details (name, gender, age)
exp_info = {"Age": "", "Gender": ["Male", "Female", "Other"], "Participant": ""}
dlg = gui.DlgFromDict(dictionary=exp_info, title="Emotional Stimuli Experiment")
if not dlg.OK:
    core.quit()

# Validate age input
if not exp_info["Age"].isdigit():
    dlg = gui.Dlg(title="Error")
    dlg.addText("Please enter a valid numeric age.")
    dlg.show()
    core.quit()

# Parameters
n_trials = 32
trial_duration = 1.5
iti_duration = 0.2
images_path = './images'

# Load image data
data = pd.read_csv("final_data.csv").reset_index(drop=True)

# Create window
win = visual.Window(size=(960, 720), color="black", units="pix")

instruction_text = visual.TextStim(win, text="", pos=(0, 0), color="white")
fixation = visual.TextStim(win, text="+", pos=(0, 0), color="white")

if not os.path.exists("data"):
    os.makedirs("data")

# Display instructions
instruction_text.text = (
    'Please categorize the images according to the instructions below: \n\n'
    'Press the "I" button if the image on the screen is indoors.\n'
    'Press the "O" button if the image on the screen is outdoors.\n\nPress any key to start.'
)
instruction_text.draw()
win.flip()
event.waitKeys()

# Open data file
filename = os.path.join(
    "data",
    f"{exp_info['Participant']}_{exp_info['Gender']}_{exp_info['Age']}.csv"
)
with open(filename, "w") as data_file:
    # Write headers
    data_file.write("trial,emotional_class,category,response,correct,rt,participant,gender,age\n")

    # Run trials
    for i in range(min(n_trials, len(data))):  # Ensure trials do not exceed the data length
        category = data["Category"][i]
        emotional_class = data["Class"][i]
        image_path = os.path.join(images_path, f"{data['Theme'][i]}.jpg")

        # Check if image exists
        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}")
            continue

        # Display image
        image_stim = visual.ImageStim(win, image=image_path, size=(960, 720))
        image_stim.draw()
        win.flip()

        # Record response
        clock = core.Clock()
        response = None
        while clock.getTime() < trial_duration:
            keys = event.getKeys(keyList=["i", "o"], timeStamped=clock)
            if keys:
                response, reaction_time = keys[0]
                break

        # Check response
        correct = (category == "Inside" and response == "i") or (category == "Outside" and response == "o")
        response_status = "True" if correct else "False"
        reaction_time = reaction_time if response else "NA"

        # Write trial data
        data_file.write(
            f"{i},{emotional_class},{category},{response},{response_status},{reaction_time},"
            f"{exp_info['Participant']},{exp_info['Gender']},{exp_info['Age']}\n"
        )

        # Inter-trial interval
        fixation.draw()
        win.flip()
        core.wait(iti_duration)

# Close the window
win.close()
core.quit()
