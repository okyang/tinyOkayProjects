# Author: Owen Yang
# Description: Quick script to generate dependent files.

codeDIR = input("input path to pir_activated_cam directory:")

# === generate autostart .desktop file ===
with open("pac_startupTemplate.desktop","r") as startupTemp:
    # read
    startupTemplateText = startupTemp.read().format(codeDIR)

    # write
    with open("pac_startup.desktop", "w") as startupOut:
        startupOut.write(startupTemplateText)

# === generate bash script to be run ===
with open("runFromStartupTemplate.sh","r") as runFromStartTemp:
    # read
    runFromStartupTemplateText = runFromStartTemp.read().format(codeDIR)

    # write
    with open("../runFromStartup.sh", "w") as runOutput:
        runOutput.write(runFromStartupTemplateText)

print("dependent files successfully generated")
