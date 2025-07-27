Here’s your cleaned-up and reformatted transcript. The structure has been improved for clarity and readability, and **important keywords, concepts, and code elements** have been bolded throughout, while preserving the original tone and intent.

---

Let’s now discuss the **fundamental building blocks of GitHub Actions**.

There are **three main building blocks**: **workflows**, **jobs**, and **steps** (which exist within jobs). Let’s go through each one in detail to understand their differences.

---

### **Workflows**

**Workflows** are defined at the **repository level**, meaning whenever we want to create a workflow, we must do so **within a repository**. They also define which **triggers** actually start the workflow. This trigger configuration happens at the **workflow level**, not the job or step level.

A workflow is composed of **one or more jobs**—we can define a single job or multiple jobs per workflow.

---

### **Jobs**

**Jobs** are defined **within workflows**; they cannot exist outside of them. Jobs specify the **execution environment**, which can be **Linux**, **Windows**, or **macOS**. We’ll explore the differences between these environments in a later lecture.

Each job contains **one or more steps**. By default, **jobs run in parallel**—if you create ten jobs without specifying dependencies, they will **all run at the same time** when the workflow is triggered.

---

### **Steps**

**Steps** are defined at the **job level** and represent the actual **scripts or GitHub Actions** that are executed. Steps **run sequentially by default**—and in fact, this is **always** the case. If you want steps to run in parallel, you need to **place them in different jobs**, then configure those jobs to run concurrently.

---

### **Clarifying GitHub Actions Terminology**

If you're new to GitHub Actions, some confusion around the term "GitHub Action" is natural. Let's clarify the terminology:

* At the top level, **GitHub Actions** refers to the **entire CI/CD platform** provided by GitHub. This includes workflows, custom actions, runners, and more.
* A **workflow** defines the automation pipeline—a structured process that runs based on triggers.
* A **GitHub Action** (in lowercase) refers to a **reusable piece of code** (often from another repository or the GitHub Marketplace) that you can execute in a step. Instead of writing shell commands directly, you can reference an action like `actions/checkout@v3`.

So:

* **GitHub Actions** = the overall CI/CD feature
* **Workflow** = a file that defines automation
* **Action** = a reusable, shareable unit of code used inside a step

As you get hands-on, these distinctions will become clearer. But if anything remains confusing, don’t hesitate to ask questions—I'm happy to help clarify.

---

### **Connecting Concepts with a Workflow Example**

On the right side of your editor, you may see a visual representation of the components we just discussed: **workflows**, **jobs**, and **steps**.

The whole file is a **workflow**. If you were to copy and paste it into a GitHub repo, it would run (assuming it's placed correctly and syntactically valid). Within the file:

* The **workflow name** is defined at the top.
* The **trigger** is specified using the `on` key.
* Under the `jobs` key, we define multiple **jobs**.
* Each job specifies a `runs-on` key that defines the runner environment (e.g., `ubuntu-latest`).
* Each job contains a `steps` array that defines **individual steps**.

Keep in mind: each job runs on a **separate virtual machine**, even if they use the same OS image. So, there's no shared state between jobs unless explicitly passed.

---

### **Creating Our First Workflow File**

Let’s create a simple, yet fully functional GitHub workflow to reinforce these concepts.

1. Create a directory structure:

   ```bash
   mkdir -p .github/workflows
   ```

2. Inside the `workflows` folder, create a file called:

   ```
   01-building-blocks.yaml
   ```

3. Open this file in your editor. If you see a squiggly error line, it's likely from the **GitHub Actions extension** in **VS Code**.

   * You can install this extension by searching for **"GitHub Actions"** in the Extensions Marketplace.
   * It provides useful features like **YAML validation** and **inline documentation**.

---

### **Writing the Workflow File**

Here’s the initial structure:

```yaml
name: 01-building-blocks

on: push

jobs:
  echo-hello:
    runs-on: ubuntu-latest
    steps:
      - name: Say Hello
        run: echo "Hello World"
```

**YAML indentation is crucial.** Whether you use two or four spaces doesn’t matter, as long as it's **consistent**. For example, under `jobs`, all nested keys must be properly indented.

---

### **Adding a Second Job**

Now let’s add another job that demonstrates a **failed step**:

```yaml
  echo-goodbye:
    runs-on: ubuntu-latest
    steps:
      - name: Failed Step
        run: |
          echo "I will fail"
          exit 1
      - name: Say Goodbye
        run: echo "Goodbye"
```

What happens here is:

* The **first step** fails with `exit 1`.
* The **second step** (`Say Goodbye`) is **skipped**.
* This is the default behavior: **if a step fails, all following steps in that job are skipped**.

You’ll see this behavior reflected in GitHub’s **Actions tab** with a red X for failed steps and a gray dash for skipped ones.

---

### **Observing Workflow Execution on GitHub**

After committing and pushing the changes:

```bash
git add .
git commit -m "Add building blocks workflow"
git push
```

On GitHub:

* Navigate to the **Actions** tab.
* You’ll see a yellow dot (queued), then red (failed) icon.
* Clicking into the workflow run will show:

  * `echo-hello` job succeeded.
  * `echo-goodbye` job failed.
  * Only the **first step ran**; the second step was **skipped**.

This illustrates the default **execution flow and error handling** in GitHub Actions.

---

### **Updating the Failing Step to Succeed**

Let’s now modify the failed step to **succeed**:

```yaml
- name: Successful Step
  run: |
    echo "I will succeed"
    exit 0
```

Now push your changes again:

```bash
git add .
git commit -m "Fix failed step"
git push
```

Back on GitHub:

* A new workflow run will be triggered.
* Both steps will now **execute successfully**.
* You’ll see **green check marks** for both.

---

### **Summary**

In this first practical exercise, we:

* Defined a **workflow** file named `01-building-blocks.yaml`.
* Used the `on: push` trigger to initiate workflow runs.
* Created **two jobs**: `echo-hello` and `echo-goodbye`.
* Used **basic shell commands** within **steps** to simulate success and failure.
* Observed the default **step execution flow**—where a failed step prevents subsequent steps in the same job from running.

We also explored the **GitHub Actions VS Code extension**, which enhances the editing experience with documentation, validation, and helpful hints.

In the next lecture, we’ll expand on this foundation with more complex workflows and deeper exploration of **execution flow control** in GitHub Actions.

Let’s take a short break and continue soon.
