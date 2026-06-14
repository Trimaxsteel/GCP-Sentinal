from flask import Flask, render_template, request
from scanner import EnterpriseCloudScanner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', results=None)

@app.route('/scan', methods=['POST'])
def scan():
    target_id = request.form.get('project_id', '').strip()
    scanner = EnterpriseCloudScanner()
    
    all_results = []
    
    if target_id.upper() == "ALL":
        for target in scanner.critical_targets:
            results = scanner.run_multi_vector_audit(target)
            all_results.extend(results)
        display_target = "Global Audit: 5 High-Value Public Assets"
    else:
        all_results = scanner.run_multi_vector_audit(target_id)
        display_target = target_id

    # Generate professional statistics
    stats = {
        "target": display_target,
        "total": len(all_results),
        "critical": len([f for f in all_results if f['sev'] == 'CRITICAL']),
        "high": len([f for f in all_results if f['sev'] == 'HIGH']),
        "medium": len([f for f in all_results if f['sev'] == 'MEDIUM']),
        "low": len([f for f in all_results if f['sev'] == 'LOW'])
    }
    
    return render_template('index.html', results=all_results, stats=stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)