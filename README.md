## Flask Application Design

**HTML Files**

* **index.html (Homepage):** The entry point of the application. It will contain the form for defining experiments.
* **results.html (Results Page):** Displays the collected experimental results and metrics for analysis.

**Routes**

* **index:**
    - HTTP GET: Renders the `index.html` homepage.
    - HTTP POST: Collects experiment details from the form submission and stores them in a database.
* **submit:**
    - HTTP POST: Stores the submitted experiment details, including the experiment name, variables, and metrics.
* **results:**
    - HTTP GET: Queries the database for all experiments and their respective results.
    - HTTP POST: Processes experimental results and metrics, updating the database accordingly.
* **analysis:**
    - HTTP GET: Renders the `results.html` page, displaying the experiments, results, and metrics for analysis.

**Functionality**

1. **Experiment Definition:** Users can define experiments on the homepage, specifying the experiment name, variables, and metrics.
2. **Experiment Submission:** Experiment details are stored in a database upon form submission.
3. **Results Collection:** The application collects experimental results and metrics over time.
4. **Results Analysis:** Users can analyze the collected experimental results and metrics on the "Results" page.
5. **Rapid Prototyping:** The defined experiments facilitate rapid prototyping by allowing users to quickly iterate through different experiment configurations, collect results, and analyze them.

**Metrics and Success**

* **Metrics:** The application will track experiment-specific metrics to measure the success of each experiment.
* **Success:** The success of an experiment is determined by achieving the desired results as defined by the experiment's metrics.