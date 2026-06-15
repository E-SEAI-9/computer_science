# Creating and manipulating files and directories

1.  **Launch the Terminal.**

    - **Action:** This is a manual step. Open your Terminal application. You'll likely start in your home directory (`~`).

2.  **Create a new project directory.**

    - **Command:**
      ```bash
      mkdir my_project
      ```

3.  **Change your current directory to `my_project`.**

    - **Command:**
      ```bash
      cd my_project
      ```
    - **Hint:** Use **Tab Completion**\! Type `cd my` and press `Tab`.

4.  **Create two subdirectories: `src` and `test`.**

    - **Command:**
      ```bash
      mkdir src test
      ```
    - **Hint:** The `mkdir` command can create multiple directories at once.

5.  **Confirm the subdirectories exist.**

    - **Command:**
      ```bash
      ls
      ```
    - You should see `src` and `test` listed as the output.

6.  **Move into the `src` directory and create a new file.**

    - **Commands:**
      ```bash
      cd src
      touch main.txt
      ```

7.  **Add a simple line of text using `echo`.**

    - **Command:**
      ```bash
      echo "This is the first line." > main.txt
      ```

8.  **Check the file’s contents with `cat`.**

    - **Command:**
      ```bash
      cat main.txt
      ```
    - You should see `This is the first line.` printed in your terminal.

9.  **Open `main.txt` in VS Code from the Terminal.**

    - **Command:**
      ```bash
      code main.txt
      ```
    - **Hint:** If this command doesn't work, you need to set up the `code` command in VS Code. Open VS Code, press **`Shift + Command (⌘) + P`**, type `Shell Command: Install 'code' command in PATH`, and press Enter.

10. **Save your changes and close VS Code.**

    - **Action:** Add a new line like "This line was added in VS Code." inside the editor, save with **`Command (⌘) + S`**, and close the window or tab.

11. **Move up one directory to `my_project`.**

    - **Command:**
      ```bash
      cd ..
      ```

12. **Copy `main.txt` from the `src` folder to the `test` folder.**

    - **Command:**
      ```bash
      cp src/main.txt test/
      ```
    - **Hint:** The `cp` command structure is `cp <source_path> <destination_path>`.

13. **Move into the `test` directory to verify the copy.**

    - **Commands:**
      ```bash
      cd test
      ls
      ```
    - You should see `main.txt` listed here.

14. **Rename `main.txt` to `main_test.txt`.**

    - **Command:**
      ```bash
      mv main.txt main_test.txt
      ```
    - **Hint:** The `mv` command is used for both **moving** and **renaming** files. Renaming is just "moving" a file to a new name in the same location.

15. **Open `main_test.txt` in VS Code and add a new line.**

    - **Command:**
      ```bash
      code main_test.txt
      ```
    - **Action:** Add a line like "This is a test file." to the content.

16. **Save and close VS Code.**

    - **Action:** Manual step.

17. **Go back to the `my_project` directory.**

    - **Command:**
      ```bash
      cd ..
      ```

18. **List all contents recursively to see the final structure.**

    - **Command:**
      ```bash
      ls -R
      ```
    - **Hint:** The `-R` flag stands for **Recursive**. It lists the contents of the current directory and then lists the contents of all its subdirectories.

19. **(Optional) Clean up by removing the project directory.**

    - **Commands:**

      ```bash
      # First, move out of the project directory to avoid errors
      cd ..

      # Now, remove the directory and all its contents
      rm -rf my_project
      ```

    - **[EXTRA INFO] ⚠️ Important Safety Warning:** As always, be extremely careful with `rm -rf`. It permanently deletes everything in the specified path without confirmation. Make sure you are in the correct location before running this command.
