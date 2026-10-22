<h1 align="center">FRANK VALDEZ</h1>

<p align="center">Code. Curiosity. A little fun with it.</p>

<h2 align="center"><a href="https://frankstop.github.io/portfoliotest1/">MY PORTFOLIO! ↗</a></h2>

```text
       +---+---+---+---+---+
       | F | R | A | N | K |
       +---+---+---+---+---+
                  a little corner of the web.
```

Selected projects, tiny interactive experiments, a colorful cow, and a clock that keeps going. Built with plain HTML, CSS, JavaScript, and Canvas. No extensions, packages, or build step needed.

## Take a look around

```text
       [ PROJECTS ] ---- [ PLAY ] ---- [ HERE & NOW ]
```

- **Projects:** selected GitHub repositories, code-update dates, language breakdowns, and engineering notes.
- **The mini player:** stir a flow field, move a particle orbit, or make ripples. Pause, restart, or expand the player.
- **A little fun:** click the cow for another thought and check the live local clock.

Experiments pause when offscreen or when the tab is hidden. Reduced-motion preferences start them paused. Project data stays available from a saved snapshot when GitHub cannot be reached.

## Run it locally

```text
       .-----------------------.
       | > hello, localhost_   |
       '-----------------------'
```

From this folder, run:

```sh
python3 -m http.server 8000 --directory dist
```

Open [localhost:8000](http://localhost:8000). On Windows, use `py` instead of `python3`. Keep the local server running so the project data can load.

## Inside the folder

```text
       portfoliotest1/
       |-- dist/          website, project data, and local fonts
       |-- scripts/       project-data refresh and Pages setup
       '-- .github/       automatic Pages deployment
```

Edit the website in `dist/`. Refresh the saved public GitHub metadata with:

```sh
python3 scripts/refresh-projects.py
```

Project descriptions and engineering notes are reviewed separately. Language percentages reflect GitHub's code-byte counts, not proficiency; the Othello counts include its checked-in virtual environment. Fonts are hosted locally, with their license included in the assets folder.

## Put it on the web

```text
       [ commit ] ------> [ GitHub Pages ] ------> hello, world.
```

The included workflow publishes `dist/` when changes reach the repository's default branch. To enable it, choose **Settings → Pages → Build and deployment → Source → GitHub Actions**, then run **Deploy portfolio** from the Actions tab.

Alternatively, with GitHub CLI installed and signed in to an account that can administer the repository, run:

```sh
sh scripts/enable-pages.sh
```

This sets the short repository description and website link, and enables Pages with GitHub Actions. Commit and push the included files to the default branch to trigger deployment. The portfolio link above will work after the first successful deployment.

```text
        ___________________________
       < Have a little fun with it. >
        ---------------------------
               \   ^__^
                \  (oo)\_______
                   (__)\       )\/\
                       ||----w |
                       ||     ||
```

[GitHub](https://github.com/frankstop) · [All repositories](https://github.com/frankstop?tab=repositories)
