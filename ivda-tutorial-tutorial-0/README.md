## Tutorial Set

Hi and welcome to the tutorial set on how to build an IVDA app. Together, we will build an exemplary webapp in 9 steps using Vue.Js and Python where you will learn the foundations of the involved technologies and their interplay.
Each tutorial set is further accompanied by references where the concepts needed are explained in more detail.

### Tutorial-0: Frontend Boilerplate Code

#### Install Vue.js and create a Project
In the first couple of steps, we will install vue.js and create a basic boilerplate project. This web framework was chosen because it is one of the easiest to learn but still has all the functionalities of a modern web framework.

1. Install npm and node through the node.js website. Install the recommended version.
- check in terminal/cmd that the node version > 16.15: ``node -v``
- check npm version > 8.3.0: ``npm -v``
2. Create an empty folder with the name “example-project”.
3. Open the empty folder in the command line / terminal.
4. (sudo) ``npm install -g @vue/cli``
5. Create a Vue project with “vue create hello-world” using the command line.
6. select Vue 2 with arrows + enter

<img src="0_vue_create_project.PNG" alt="drawing" width="400"/>

7. Open the folder "hello-world" inside "example-project" in preferably Webstorm (free for students with educational package) or alternatively using visual studio code.
- For Webstorm, it's your best option to download the jetbrains toolbox
- For VS Code, install a vue extension if the vue syntax is not recognized (e.g. Vue 3 Snippets by hollowtree)
8. Open a terminal inside Webstorm and run: ``npm install``
9. Then, run in the same terminal ``npm run serve`` and navigate to localhost (highlighted link in the terminal).
   Congrats! Your first Vue.js App is running!
<details open><summary>Screenshot</summary>
<img src="0_first_vue_project.PNG" alt="drawing" width="400"/>
</details>

#### Install the Vuetify Library
In the next couple of steps we will add the Vuetify library to our project. This will help us to for the styling and layout of the webapp.
1. Inside the terminal of the IDE, terminate the Frontend with "ctrl + c".
2. Add the Vuetify library with ``vue add vuetify`` (ignore any git related warning and proceed)
3. Use the Default option (Vuetify for Vue 2) and press enter.

<img src="0_add_vuetify.PNG" alt="drawing" width="400"/>

4. Run ``npm run serve`` inside the IDE terminal and your project with vuetify should build. Then, navigate to localhost.
<details open><summary>Screenshot</summary>
<img src="0_vuetify.PNG" alt="drawing" width="400"/>
</details>

#### References
[Install Webstorm](https://www.jetbrains.com/help/webstorm/installation-guide.html)\
[Vue.JS 2 Tutorial (Youtube Playlist) #1 - #5](https://www.youtube.com/watch?v=5LYrN_cAJoA&list=PL4cUxeGkcC9gQcYgjhBoeQH7wiAyZNrYa)\
[Vuetify Tutorial (Youtube Playlist) #1 - #3](https://www.youtube.com/watch?v=2uZYKcKHgU0&list=PL4cUxeGkcC9g0MQZfHwKcuB0Yswgb3gA5)
