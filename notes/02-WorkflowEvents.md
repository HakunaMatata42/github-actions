## **Workflow Events in GitHub Actions - Theory**

In this lecture, we will discuss **workflow events** and how they can be used in **GitHub Actions**.

Basically, **events** in workflows are **triggers** - so we can think of events as different triggers. There are many ways that we can trigger **GitHub workflows**.

### **Repository-Level Events**

The first group here is if an event happened at the **repository level**. Examples would be a **push** to the repository. We can also specify different **branches**. We can filter some of the events and we'll discuss that later on - an event related to **issues** for example, an issue is created or it is updated.

There are events also related to **pull requests**. If a pull request is opened, is closed, it's synchronized. There are also events related to **pull request reviews**, **forks** and many, many more.

So there are many events here. I will show you in a few minutes the page from **GitHub**, the documentation where you can find all the available events. But first of all, let's understand the groups here.

### **Manual Triggers**

The second group is a **manual trigger**. So we can trigger workflows from the **UI** as long as we specify the trigger in the **GitHub YAML file**. The button to trigger the workflow in the UI is going to become available.

We also can trigger workflows via **API calls**, and we can trigger workflows from within **other workflows**. Later on, we will discuss the concept of **reusable workflows**, and we will see how this happens in practice.

### **Scheduled Triggers**

And the final group is the **schedule**. We can actually run a workflow as a **cron job**, as long as we specify the schedule for the workflow as a **cron expression**, and this will enable us to run the workflow automatically without us having to go and click on the UI or trigger it via an API call, or from within another workflow.

### **GitHub Actions Events Documentation**

If you run a simple Google search for **GitHub Actions events**, the first link that appears tells us all the events that trigger workflows. You can also find this page here via the **GitHub Actions documentation** using **workflows**, and then the section here **events that trigger workflows**.

As you can see here on the right, there are so many events and there are many different things that we can add to our **workflow file**. This is extremely flexible, which means that it will probably and most likely offer the type of event that you need for a specific situation.

The most used ones are **labels**, **issues** or we have here the **push**. And this is also very, very much used. Or whenever you have a **release** here, for example, or a **pull request** or a **pull request review**. So these are the most common ones.

But nonetheless we have events for everything - **deployments**, **project related events** and many more. And as we scroll here then you can see that it defines both the **event** as well as the different variations or the different **activity types** within this event here that we can mention in our workflow.

We're going to discuss that in the **activity type** section. But for now just get familiar with this documentation. I think it's useful for you to already know that it exists. And here you can see at the bottom how we can actually use that. Once we gather the types here in our activity type section, then you understand exactly what this means.

For now, you can simply think, if we go here down to the **push event**, you will see this is very similar to what we have done in our first practical exercise. The only difference here is that this is in a new line.

And as it happens, we can specify **multiple triggers** for the same workflow. We just have to provide here an **array** instead of a single entry. And this will allow us to run the same workflow in case different events happen.

So much for the theoretical discussion. I would recommend you keep this page somewhere accessible, or you can always find it via Google because there is of course no need for you to memorize all these things. You're not expected to do that at any point in time, but it's good to know that there is a good, very comprehensive documentation you can always refer to whenever you are looking for a specific event in **GitHub Actions**.

With that in mind, let's take a short break and come back to our **workflow events** practical exercise.

---

## **Workflow Events - Practical Exercise**

Welcome. Let's now discuss **workflow events** in a second practical exercise. We're going to start by creating a new file under the **`.github/workflows`** folder. And we're going to call this file **`02-workflow-events.yaml`**. The **`.yaml`** is important here. Once again that's the extension we have to use.

### **Setting Up the Workflow File**

And we will define a **name** here. And this name is going to be **`02-workflow-events`**.

Now here the main focus of this lecture is to discuss the **`on`** property of the job. So let's start by writing down **`push`** here and let's get the **jobs** section out of the way, because we want to then focus on how we can expand the **`on`** section here so that we can add more triggers.

Let's have a simple job. This is going to be called **`echo`**. And this is going to **`run-on: ubuntu-latest`**. And this is going to have a single **step**. And within the **steps** here we're going to add an **array**. So the **dash** to identify the first element of the array.

And the **name** here is simply going to be **"Show the trigger"**.

### **Accessing GitHub Context Information**

Now when we execute. And here we can add a **`run`**. And when we run - when we create a workflow - **GitHub** provides us a lot of information around different factors here that are related to the workflow. One of these things is the **event** that triggered this workflow.

So how can we access that? Let's simply **echo** and we'll say **"I've been triggered by a"**. And then here we can access the event by using this interesting pattern - the **dollar sign**. And then **curly brackets curly brackets**. So **double curly brackets** here.

And then we can use **`github.`**. And you can see that this provides a lot of things that we can use here. All of this is available as we start running our workflow. This is all provided by **GitHub**. We will discuss - this is called a **context**. The **GitHub context** - we'll also discuss this in details.

But the only thing that we're interested here is the **`event_name`**. Now if we hover over the **`event_name`** here, then you will see that we have a little documentation that says that this is going to give us the name of the event that trigger the workflow run.

So we're going to simply say interpolate this value here with an **echo** statement. And then we can use this syntax. This is specific to **GitHub Actions**. And this allows us to then retrieve the value of the event that triggered this workflow. And then we're just going to add something like this.

And that's it for the section here in our job. So this is the first version of this file. Let's save this.

### **Committing and Testing the Initial Workflow**

And now in our terminal we can **`git add .`**. And then we can **`commit`** with whatever message you would like to commit. Once you write your message simply commit this and then **`push`**.

Let's now jump to **GitHub** and see the result of this run here. Once we are in **GitHub**, we can come under the **Actions** tab here. And now you will see that we have two workflows mentioned here. Once again these are the **names** that we define in the **workflow files**.

And if you look carefully you will see that there are **two workflow runs** here. Why is it so? Well remember that we have our first workflow which is the **building blocks workflow** and this workflow here. If we click on any of the runs and you can see that once I click on the specific workflow, it simply shows the - or it only shows the flows related to the execution runs related to that workflow.

And if we click here, we can then **view the workflow file**. And remember this is also triggered **on push**. That's why we are seeing here two workflow executions once we push the code to **GitHub**.

Now let's have a look at our **`02-workflow-events`** one. And we want to see the result of this. So if we open it and then we open the **echo** statement and we **show the trigger**, then we will see that **"I have been triggered by a push event"**.

### **Adding Multiple Triggers**

Let's now add more entries here to our **`on`** key, so that we can trigger this workflow from different events. And we can either specify this as an **array**. So for example we can add **`push`**. And then we could say here for example **`pull_request`** right. This is possible.

We can also specify this as an **object**. So if we were to add it like this **`push:`** and a **colon** and **`pull_request:`** and a **colon**. This is also valid syntax. And I do prefer this one, this syntax here because then it already prepares this workflow. It already gives the possibility of customizing, for example, the **pull request**. We might be interested in running only for a specific **branch**, or only if the pull request is created. And we can then customize this same thing for **push** right? We can filter by **branch name**, and we can customize this more easily if we already have the **object format**.

So I would leave it as it is. It's also possible to use the **array** if you prefer to do so, but I like this format a little bit more.

### **Adding Schedule Trigger**

Let's now add another one here. And this is going to be the **`schedule`** one. And the **`schedule`** one. We're going to add here an entry. You can see that there is an error here. And once we hover over this is an unexpected value. That is because of the **indentation** here right. So the indentation needs to be fixed.

And once we fix that then you can see here that there is another error that says hey we are expecting something for this **schedule**. And this is an **array**. This is a **list**. And we can simply pass **`cron`** and then a **cron expression**.

Now if you look here this is going to tell you hey this is not a valid **cron expression**. So lots of validation going on here. Very helpful.

### **Understanding Cron Expressions**

Let's have a look at what we or how we can generate how we can create a **cron expression**. This is more if you are not familiar with the **cron syntax**, but I just want to then have a look here in the **cron expression generator**. And I did check two of them beforehand. Just want to highlight something here.

If you go with the first one and you will see that it has **six digits** right. So it has a **seconds**, **minutes**, **hours**, **days**, the **day**, **month** and **year**. Now if we were to use this in **GitHub Action** with the six digits here for the - or the six elements for **cron**, this would give us an error.

Let's just try to use it here. We're going to say **`0 0`** and then **`* * * *`**. And as you can see as soon as we add six elements this is not supported with **five elements**. That is fine.

So we're going to go with this syntax here. Luckily for us this is how the second one works. So we can just come here. And then you can start defining. So if you want to run for example at **zero minutes** **zero hour** of every day, then you would simply say **`0 0`**. And then it runs every day at **12 a.m.** Right?

So if you then want to specify a certain day of the month and a certain month of the year or even a day of the week, then you can do that by specifying this, **asterisks** here, if we do not specify them, then simply means **all** right, so here, instead of doing it like so we can actually run this workflow **every five minutes**. For example, it's going to run every five minutes. It's going to run every ten minutes.

And **GitHub Actions** or **GitHub** supports, the granularity of running up to **every five minutes**. So if you were to try to run **every minute**, that would not be supported. So we will go with the **every five minutes** expression. We can just copy this and paste here in our **IDE**. Right. So now no errors with **cron**.

### **Adding Manual Trigger**

And we can add one more here. And this is called is a very good one. It's called **`workflow_dispatch`**. And **`workflow_dispatch`** is the **manual trigger** from the **UI** that we have discussed in the slides. By adding this here to our **`on`** keyword, this will enable us triggering the workflow from the **UI**.

Okay, so I think this is a good example. There are different ways here that we will trigger the workflow. We will now go to **GitHub Actions** and we will try all of them. But before we just need to **`git add`** this and then **commit** with whatever message you want, I'll simply save it like this. Let's now **push** this and go to **GitHub**.

### **Testing Manual Trigger**

Back in **GitHub**, if we click here on the **Actions** tab, then you see again our runs started. And now if we click on **`02-workflow-events`**, we will see that there is a new section here on the page that says that this workflow has a **Workflow Dispatch Events** trigger. Therefore, we can trigger the workflow by clicking here and selecting the **branch**.

Once we click on **"Run workflow"** and we refresh the page, it might take a few seconds to appear. This is already here for us. Simply **manually run** by me. Now once we click here and we inspect the result of the **echo** statement, then we will see that this was triggered by a **workflow_dispatch event**.

So this is different than the one we had before. And if we were to come back here and click on the second one or rather the second one on the list, then we will see that this is different. This was triggered by our **push**.

### **Testing Pull Request Trigger**

Let's now see if we can trigger the workflow from a **pull request**. For that we have to come here and create a **new branch**. So let's **view all the branches** and we'll **create a new branch**. And this is going to be simply **`test-workflow-trigger`** right. We will branch out from **main**. We can click on **create a new branch**.

And then under our **code** here we can select the branch or rather here right. **Main**. And we can select **Test Workflow Trigger**. And then as you can see here there is something running. We're going to come back to this in a bit.

And let's just try to edit this. We are not going to merge this pull request. We just want to see that this has been edited, and then we will **commit the changes** we will commit it directly to the **test workflow trigger** branch, **commit the changes** here, and then we can **open a pull request** by here.

Comparing the **test workflow trigger** with the **main** base branch, and then simply clicking on **create the pull request**. This here opens up the **pull request**. And as you can see, we also have a couple of things that got triggered here.

And as you can see, if we **show all the checks** some of them are due to **push**, right. So this were the pushes that we have executed once we have committed to the branch. And then this is the event that was triggered by the **pull request**. If we click here on the **details** then we will see that under the event here we - it has been triggered by a **pull_request event**.

### **Testing Schedule Trigger**

As you can see this is fairly recent here. That's why the **cron job** didn't appear yet. But if we wait a few minutes and then we refresh the page, we should be able to see it after waiting a few more minutes here. As you can see, the workflows are not run yet, so.

So I did a little bit of research and as it happens here, there are some comments saying that even after we set to run **every five minutes**, it runs in **15 minutes**. Right. So it might be the case that there is some delay until **GitHub** registers and runs the workflow for the first time. We're going to wait a few more minutes and see what happens.

And just as I was speaking and I was showing you the other tab, I came back here. And as you can see, here is our first run from the **cron schedule**. Right. You can see here that this is a **scheduled workflow run**. And if we were to click here and then have a look at the logs, then we will see that this was triggered by a **schedule event**.

Perfect. So we have explored different types of **triggers**.

### **Cleanup and Best Practices**

As I mentioned in the previous lecture, when we go through the documentation, there are many more you can try before we wrap up this practical exercise, let's just go back to our **workflow file**. And we're going to actually do that from the browser here. If we go back to **workflow events**. And then here we click anywhere. And then we **view the workflow file**.

We can actually edit the file directly on the browser. And the only thing I want to do is I just want to remove the **schedule** here, because I just don't want this workflow to run **every five minutes**. Otherwise we'll have a ton of runs on our **action** step and it can get confusing.

So if we just leave **on push** **pull_request** and **workflow_dispatch**, that's okay. You could also remove the **push** one here if you want to, so that we don't trigger this workflow every time we push to this repository. Actually, maybe this is even better. So I'm just going to **commit these changes** here. And we will say now you can add whatever message you want to I will follow the pattern here. And then we can just click on **Commit changes**.

Once we do that we can also come back here to the **code**. We can have a look at **all the branches**. And then we can simply remove this **test workflow trigger** here. Let's **delete** it. It's no problem. And then the **pull request** here should also be closed. Right. So we're just doing a little bit of cleanup. And now we have just the **main branch** here. Perfect.

We can also come here to the **workflows**. And in the first workflow we can actually edit this to use the **workflow_dispatch** instead of **push**. So that we don't rerun this workflow again every time we push to the **main branch**.

So normally I'll follow this convention. I waited until this lecture to change this, and the convention I would like to follow is as we are working on a certain **workflow file**, we'll normally have the **push event** here triggering the workflow. But then once we are done, we will set this to **workflow_dispatch** so that we can focus on specific workflows at a time.

Once we **commit the changes** here and then **commit directly to the main branch**. Once we do that, then we will have everything fine here in our **GitHub** page. And if we refresh this, you will see that nothing was triggered. Right?

So if we come here to the **actions**, you will see that the last commit that triggered something was this **reduce triggers** here and not so the last commit when we change the trigger from **push** to **workflow event** did not trigger any workflow. And that's intended because we have removed the **on push** trigger.

Great. I think that's enough for this exercise. As we again advanced on the course, we will come back to these **triggers** and try different variations. But for now, I think it was a very good way of exploring the different ways that we can trigger **workflows**.
