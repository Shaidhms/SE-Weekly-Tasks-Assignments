
## 📌 [Task: Building a prompt for a niche skill using the R-T-C-F-R prompting technique](#task)

---

## 🔹 Prompt

<details>
<summary>Click to view the Prompt</summary>
  

```bash  
Role: 
You are a Performance Testing Strategist. Your task is to develop and outline a comprehensive performance testing strategy.

Task:
Create a detailed performance testing strategy for a given system, application, or service.

Context: 
The strategy should be tailored to the specific needs of the project. This includes identifying the system under test, defining the performance goals and metrics (e.g., response time, throughput, resource utilization), outlining the types of tests to be conducted (e.g., load, stress, endurance), and specifying the tools and environments to be used.

Few-Shot (Example):

- Input: 
  "Create a performance testing strategy for our new e-commerce website."  
- Output:
  - Performance Goals: 95% of all pages should load in under 2 seconds. The system should handle 10,000 concurrent users with a 99% uptime.  
  - Test Types:  
    - Load Testing: Simulate 5,000 to 10,000 users over 30 minutes to identify performance bottlenecks.  
    -  Stress Testing: Gradually increase the user load beyond 10,000 to find the system's breaking point.  
    -  Endurance Testing: Run a continuous load of 7,500 users for 24 hours to check for memory leaks or other performance degradation.  
    - Tools:Use open-source tools like JMeter for scripting and load generation. Use a tool like Grafana for real-time monitoring of server metrics.  
    -Environment:Use a dedicated, production-like testing environment to ensure accurate results.  

Report/Tone:
Provide a clear, structured, and professional report. The tone should be analytical and provide actionable recommendations. Format the output using markdown headings and bullet points for easy readability.
```
</details>

---

## 🔹 Result of the Prompt

<details>
<summary>Click to view the Result</summary>

# Performance Test Plan — E-commerce Website (Holiday Sale Readiness)

## 1) Objective and Scope

Goal:Prove the site can handle holiday-sale traffic without slowing down or failing, while keeping checkout success high.  

In scope:Web and mobile web flows for Login, Product Search, PDP, Add-to-Cart, Checkout, Payment, Order Confirmation, and critical APIs.  

**Out of scope:** Native mobile apps, seller/admin portals, long-running back-office jobs unless they are triggered by the flows above.  

---

## 2) Key Performance Indicators (KPIs) and Target SLAs

| **Area**          | **KPI**                                        | **Target**                       |
| ----------------- | ---------------------------------------------- | -------------------------------- |
| End-user response | Login p95                                      | ≤ 1.5 s                          |
|                   | Search p95 (auto-suggest + results)            | ≤ 2.0 s                          |
|                   | Product page p95                               | ≤ 1.5 s                          |
|                   | Add-to-Cart p95                                | ≤ 1.0 s                          |
|                   | Checkout steps p95 (shipping, payment, review) | ≤ 2.5 s each                     |
|                   | Order confirmation p95                         | ≤ 2.0 s                          |
| Throughput        | Orders per minute (OPM) at peak                | Business target, e.g., ≥ 250 OPM |
| Reliability       | Error rate (HTTP 5xx + functional failures)    | < 0.5% during peak               |
| Infra             | App CPU                                        | < 70% average, < 85% p95         |
|                   | DB CPU                                         | < 70% average, < 85% p95         |
|                   | GC pauses (JVM)                                | < 200 ms p95 per pause           |
| External          | Payment gateway success                        | ≥ 99.5%                          |
| Observability     | Traces with end-to-end span                    | ≥ 95% sampled during tests       |

---

## 3) Workload Model and Concurrency Assumptions

1. Traffic mix at peak hour 
   - Home/Landing: 100%  
   - Search: 70%  
   - Product page: 60%  
   - Add-to-Cart: 40%  
   - Checkout start: 25%  
   - Payment submit: 22%  
   - Order success: 20% conversion  

2. Think times 
   - Search to results: 3–5 s  
   - Results to PDP: 5–8 s  
   - PDP to cart: 2–4 s  
   - Checkout steps: 2–5 s  

3. Concurrency math (example):  
If target is **18,000 peak requests/min** across all flows with an average step time of 1.2 s, estimated concurrent virtual users ≈ (300 RPS × 1.2) ≈ **360 VUs** active per step. Add 30% headroom.

---

## 4) Test Types and Why

- Baseline test:** Validate scripts, data, and env.  
- Load test:** Confirm SLAs at peak load.  
- Stress test:** Push system beyond peak until failure.  
- Spike test:** Sudden traffic jumps (2–3×).  
- Soak test:** 4–8 hours continuous load.  
- Scalability test:** Repeat with infra changes.  
- Resilience test:** Failure scenarios (kill pods, throttle dependencies, etc.).  

---

## 5) Test Scenarios and Critical Paths

1. Anonymous browse → Search → PDP  
2. Login → Search → PDP → Add-to-Cart → Checkout  
3. Payment paths (Card, UPI, Wallet)  
4. Cart operations (Add, update, remove, coupon)  
5. Edge cases (large carts, OOS items, failed payment retry)  
6. APIs under load (Search, Cart, Checkout, Payment)  

---

## 6) Test Data and Dependencies

- Users: Distinct accounts  
- Products: ≥ 5k items  
- Coupons: Valid, expired, near-limit  
- Payments: Sandbox keys, deterministic outcomes  
- Reset: Nightly data refresh  

---

## 7) Environments and Config

- Perf env: Mirrors prod  
- Isolation: No competing jobs  
- Feature flags recorded  
- CDN: With & without cache  

---

## 8) Tooling and Monitoring

- Load tools: JMeter, k6, Gatling  
- Monitoring: APM + system + DB + cache metrics  
- Tracing: OpenTelemetry  
- Logs: Centralized  

---

## 9) Execution Strategy

- Baseline: 5 → 50 VUs, 20 min  
- Load: Ramp to peak, hold 2 hrs  
- Spike: 50% → 200% in 30s  
- Stress: Increase until failure  
- Soak: 4–8 hrs  

---

## 10) Capacity & Bottleneck Analysis

- SLA breach points  
- Scaling curves  
- DB slow queries & locks  
- Cache tuning  
- GC pauses  

---

## 11) Entry & Exit Criteria

✅ Entry: Env parity, monitoring ready, data validated  
✅ Exit: SLAs met, <0.5% error rate, no memory leak, graceful degradation  

---

## 12) Risks & Mitigation

- 3rd-party latency → Circuit breakers  
- Autoscaling slow → Pre-warm  
- DB hotspots → Batching, queues  
- Cold caches → Pre-warm  
- Payment retries → Idempotent capture  

---

## 13) Reporting

- Run book, dashboards, exec summary  
- Visuals: Throughput vs latency, error budget, heat maps  

---

## 14) Roles & Responsibilities

- Perf Engineer: Scripting, analysis  
- Devs: Fixes, profiling  
- DevOps/SRE: Env readiness  
- QA Lead: Assertions, sign-off  
- PM: Decisions, timelines  

</details>
