# Swift-Transit-Performance
<p>This project analyzes shipment transit performance using a dataset of 99 shipments. 
The objective is to flatten nested JSON tracking data, compute transit metrics, and generate detailed and summary CSV outputs for logistics evaluation.</p>

<h2>Project Structure</h2>

<pre>
Swift-Transit-Performance/
│
├── data/shipments.json
├── scripts/
│   ├── load_and_explore.py
│   ├── flatten_extract.py
│   ├── compute_metrics.py
│   ├── edge_case_handler.py
│   ├── generate_output_csvs.py
│   └── utils.py
├── output/
│   ├── transit_performance_detailed.csv
│   ├── transit_performance_summary.csv
│   └── service_type_analysis.csv
├── run_pipeline.py
├── requirements.txt
└── README.md
</pre>

<h2>How to Run</h2>

<ol>
  <li>Place your dataset at <code>data/shipments.json</code></li>
  <li>Install requirements:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<ol start="3">
  <li>Run the pipeline:</li>
</ol>

<pre><code>python run_pipeline.py
</code></pre>

<p>This generates:</p>

<ul>
  <li><code>transit_performance_detailed.csv</code></li>
  <li><code>transit_performance_summary.csv</code></li>
  <li><code>service_type_analysis.csv</code></li>
</ul>

<h2>Output Description</h2>

<h3>1. transit_performance_detailed.csv</h3>
<p>One row per shipment containing:</p>
<ul>
  <li>Tracking metadata</li>
  <li>Pickup &amp; delivery timestamps</li>
  <li>Total transit hours</li>
  <li>Facility touchpoints</li>
  <li>Inter-facility transit time</li>
  <li>Delivery attempts &amp; success</li>
  <li>Express service classification</li>
</ul>

<h3>2. transit_performance_summary.csv</h3>
<ul>
  <li>Average, median, min, max transit hours</li>
  <li>Facility statistics</li>
  <li>Delivery performance metrics</li>
</ul>

<h3>3. service_type_analysis.csv</h3>
<ul>
  <li>Average transit hours by service type</li>
  <li>Average facilities visited</li>
  <li>Total shipments per service type</li>
</ul>

<h2>Key Insights</h2>

<ul>
  <li>Average transit time: <b>94 hours</b></li>
  <li>Median transit time: <b>93.25 hours</b></li>
  <li>Average facilities visited: <b>2.83</b></li>
  <li>First-attempt delivery success: <b>63.6%</b></li>
</ul>

<h2>Assignment Requirements Covered</h2>

<ul>
  <li>Flattening nested JSON tracking data</li>
  <li>Extracting shipment &amp; event features</li>
  <li>Computing all required performance metrics</li>
  <li>Generating summary and service-based analysis CSVs</li>
  <li>Handling timestamp formats &amp; missing data</li>
</ul>

<h2>Author</h2>

<p><b>Aryan Ahmad Chaudhary</b><br>
