"""Evaluation harness for multi-agent system"""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "07-complete-system/solution"))

from main import CompleteOrchestrator


def load_golden_dataset():
    """Load test cases"""
    dataset_path = Path(__file__).parent / "golden_dataset.json"
    with open(dataset_path) as f:
        return json.load(f)


def evaluate_orchestrator():
    """Run orchestrator against golden dataset"""
    
    print("="*70)
    print(" EVALUATION: Multi-Agent System")
    print("="*70)
    
    dataset = load_golden_dataset()
    orchestrator = CompleteOrchestrator()
    
    results = {
        "total": len(dataset),
        "passed": 0,
        "failed": 0,
        "details": []
    }
    
    for test_case in dataset:
        test_id = test_case["id"]
        request = test_case["request"]
        
        print(f"\n[Test {test_id}] {request}")
        
        try:
            # Execute
            result = orchestrator.execute(request)
            
            # Validate output
            expected_keys = test_case["expected_keys"]
            has_all_keys = all(key in result for key in expected_keys)
            
            if has_all_keys:
                results["passed"] += 1
                print(f"  ✅ PASSED - All expected keys present")
            else:
                results["failed"] += 1
                missing = [k for k in expected_keys if k not in result]
                print(f"  ❌ FAILED - Missing keys: {missing}")
            
            results["details"].append({
                "id": test_id,
                "request": request,
                "status": "passed" if has_all_keys else "failed",
                "output_keys": list(result.keys())
            })
            
        except Exception as e:
            results["failed"] += 1
            print(f"  ❌ ERROR: {str(e)}")
            results["details"].append({
                "id": test_id,
                "request": request,
                "status": "error",
                "error": str(e)
            })
    
    # Summary
    print("\n" + "="*70)
    print(" EVALUATION SUMMARY")
    print("="*70)
    print(f"Total Tests: {results['total']}")
    print(f"Passed: {results['passed']}")
    print(f"Failed: {results['failed']}")
    print(f"Success Rate: {(results['passed']/results['total']*100):.1f}%")
    
    return results


if __name__ == "__main__":
    results = evaluate_orchestrator()
    
    # Save results
    output_path = Path(__file__).parent / "eval_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to: {output_path}")
