### Navigating the filesystem

1.  **Open the Terminal application on your Mac.**

    - **Action:** This is a manual step. Use Spotlight (**⌘ + Spacebar**) and type `Terminal`.

2.  **Print your current location.**

    - **Command:**
      ```bash
      pwd
      ```
    - **Hint:** This command confirms your starting point. Typically, this will be your home directory, often represented by a tilde (`~`).

3.  **Create a new directory named `practice_dir`.**

    - **Command:**
      ```bash
      mkdir practice_dir
      ```

4.  **Move into the `practice_dir` directory.**

    - **Command:**
      ```bash
      cd practice_dir
      ```
    - **Hint:** This is a great place to practice **Tab Completion**. Try typing `cd pra` and then press the `Tab` key.

5.  **Create a new, empty file named `notes.txt`.**

    - **Command:**
      ```bash
      touch notes.txt
      ```

6.  **Move back up one level.**

    - **Command:**
      ```bash
      cd ..
      ```
    - **Hint:** In the terminal, `..` is a special shortcut that always represents the **parent directory** (the directory one level up).

7.  **Print your current directory again.**

    - **Command:**
      ```bash
      pwd
      ```
    - **Hint:** The output should match what you saw in Step 2, confirming you have successfully moved back.

8.  **Remove the `practice_dir` directory.**

    - **Command:**
      ```bash
      rm -rf practice_dir
      ```
    - **Hint:** The directory is not empty, so the simple `rmdir` command won't work. We need `rm` with options:
      - `-r` stands for **recursive**, meaning "delete this directory and everything inside it."
      - `-f` stands for **force**, which prevents the system from asking for confirmation for every single file.
    - **[EXTRA INFO] ⚠️ Important Safety Warning:** The `rm -rf` command is extremely powerful and **permanent**. There is no "Trash Can" or "Undo" button. Always double-check that you are in the correct directory and deleting the right thing before pressing Enter.
