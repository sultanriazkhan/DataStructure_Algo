from flask import Flask, render_template, request, jsonify
import time
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def binary_search_algo(arr, target):
    """
    Perform binary search with detailed trace for visualization
    """
    low = 0
    high = len(arr) - 1
    iteration = 0
    trace = []

    while low <= high:
        iteration += 1
        mid = low + (high - low) // 2
        current_value = arr[mid]

        step = {
            "iteration": iteration,
            "low": low,
            "high": high,
            "mid": mid,
            "value": current_value,
            "message": ""
        }

        if current_value == target:
            step["message"] = f"✓ Target {target} found at index {mid}!"
            trace.append(step)
            return mid, trace

        elif current_value < target:
            step["message"] = f"📈 {current_value} < {target} → Moving right (search in upper half)"
            trace.append(step)
            low = mid + 1

        else:  # current_value > target
            step["message"] = f"📉 {current_value} > {target} → Moving left (search in lower half)"
            trace.append(step)
            high = mid - 1

    # Target not found
    insert_position = low
    trace.append({
        "iteration": iteration + 1,
        "message": f"❌ Target {target} not found. Would be inserted at index {insert_position} to maintain sorted order"
    })

    return -1, trace

@app.route("/", methods=["GET"])
def index():
    """Render the main page"""
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    """Handle search requests"""
    try:
        # Get and validate input
        array_input = request.form["array"].strip()
        target = int(request.form["target"])

        # Parse array (handle both comma and space separators)
        if ',' in array_input:
            arr = list(map(int, array_input.split(',')))
        else:
            arr = list(map(int, array_input.split()))

        # Sort array for binary search
        arr.sort()
        
        app.logger.debug(f"Searching for {target} in {arr}")

        # Perform binary search
        result, trace = binary_search_algo(arr, target)

        return render_template(
            "index.html",
            arr=arr,
            target=target,
            result=result,
            trace=trace
        )

    except ValueError as e:
        app.logger.error(f"Invalid input: {e}")
        return render_template(
            "index.html",
            error="Please enter valid numbers (e.g., 1,2,3 or 1 2 3)"
        )
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return render_template(
            "index.html",
            error="An unexpected error occurred"
        )

@app.route("/api/search", methods=["POST"])
def api_search():
    """JSON API endpoint for programmatic access"""
    try:
        data = request.get_json()
        array_input = data.get("array", "")
        target = int(data.get("target", 0))

        if ',' in array_input:
            arr = list(map(int, array_input.split(',')))
        else:
            arr = list(map(int, array_input.split()))

        arr.sort()
        result, trace = binary_search_algo(arr, target)

        return jsonify({
            "success": True,
            "array": arr,
            "target": target,
            "result": result,
            "trace": trace
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route("/random", methods=["GET"])
def random_array():
    """Generate random sorted array for testing"""
    import random
    size = random.randint(5, 15)
    arr = sorted(random.sample(range(1, 100), size))
    return render_template("index.html", arr=arr)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)