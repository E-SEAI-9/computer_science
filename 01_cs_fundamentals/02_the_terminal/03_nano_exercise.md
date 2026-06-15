# Command-line editors: nano

1.  **Open the Terminal and Verify Your Location.**

    - **Action:** Open your Terminal application.
    - **Command:**
      ```bash
      pwd
      ```
    - **Hint:** This confirms your starting directory, which is usually your home folder (`~`).

2.  **Create and Enter a Working Directory.**

    - **Commands:**
      ```bash
      mkdir practice_nano
      cd practice_nano
      ```

3.  **Create and Open a New File with Nano.**

    - **Command:**
      ```bash
      nano notes.txt
      ```
    - **Hint:** This command opens the `nano` editor interface directly in your terminal window. Since `notes.txt` doesn't exist yet, `nano` creates it for you.

4.  **Add and Manipulate Content.**

    - **Action:** Inside the `nano` editor, type the following lines:
      ```
      This is my first file edited with Nano.
      I can easily add more lines of text here.
      ```
    - **Practice Commands:**
      - Use the **arrow keys** to move your cursor to the second line.
      - Press **`Ctrl + K`** to cut (delete) the line.
      - Move the cursor to a new empty line at the bottom and press **`Ctrl + U`** to paste the line back.
    - **Hint:** The `^` symbol at the bottom of the `nano` screen represents the **`Ctrl`** key.

5.  **Save Your Changes.**

    - **Action:** Press **`Ctrl + O`** (the "Write Out" command).
    - **Hint:** `nano` will prompt you for the "File Name to Write". Since it's already `notes.txt`, just press **`Enter`** to confirm.

6.  **Exit Nano.**

    - **Action:** Press **`Ctrl + X`** to exit the editor.
    - **Hint:** If you had unsaved changes, `nano` would ask if you want to save them before quitting.

7.  **Verify the File’s Contents.**

    - **Command:**
      ```bash
      cat notes.txt
      ```
    - **Hint:** This command prints the contents of the file directly to your terminal, allowing you to quickly confirm that your edits were saved correctly.

8.  **(Optional) Re-edit the File.**

    - **Commands & Actions:**
      1.  Reopen the file: `nano notes.txt`
      2.  Add a new line of text.
      3.  Save the file: Press `Ctrl + O`, then `Enter`.
      4.  Exit nano: Press `Ctrl + X`.
      5.  Verify again: `cat notes.txt`

9.  **(Optional) Clean Up.**

    - **Commands:**

      ```bash
      # First, move out of the directory you want to delete
      cd ..

      # Now, remove the directory and all its contents
      rm -rf practice_nano
      ```

    - **[EXTRA INFO] ⚠️ Important Safety Warning:** Remember, the `rm -rf` command is permanent and powerful. It deletes everything without asking for confirmation. Always be certain you are deleting the correct directory.
