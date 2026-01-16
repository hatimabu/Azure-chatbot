# Azure Cost Estimate

**Last Updated:** January 2026

This document helps you understand what you'll pay when you deploy to Azure.

## 💰 Monthly Cost Breakdown

### Minimal Usage (Learning/Testing)
**Perfect for: Your first 1-3 months of learning**

| Service | Usage | Monthly Cost |
|---------|-------|--------------|
| Azure Functions | 100,000 requests/month | **$0** (1M free) |
| Cosmos DB | Serverless, light usage | **$0-5** |
| Storage Account | < 5GB | **$0** (5GB free) |
| Application Insights | < 5GB logs | **$0** (5GB free) |
| **TOTAL** | | **$0-5/month** |

### Light Usage (Small Project)
**Perfect for: Sharing with friends, small community**

| Service | Usage | Monthly Cost |
|---------|-------|--------------|
| Azure Functions | 500,000 requests/month | **$0.10** |
| Cosmos DB | 10GB storage, 100K ops | **$15-20** |
| Storage Account | 10GB | **$2** |
| Application Insights | 10GB logs | **$2** |
| **TOTAL** | | **$20-25/month** |

### Medium Usage (Active Users)
**Perfect for: Public chatbot with regular users**

| Service | Usage | Monthly Cost |
|---------|-------|--------------|
| Azure Functions | 2M requests/month | **$0.40** |
| Cosmos DB | 50GB storage, 500K ops | **$35-45** |
| Storage Account | 25GB | **$3** |
| Application Insights | 20GB logs | **$5** |
| **TOTAL** | | **$45-55/month** |

### Heavy Usage (Popular App)
**When you're successful: Many users daily**

| Service | Usage | Monthly Cost |
|---------|-------|--------------|
| Azure Functions | 10M requests/month | **$2** |
| Cosmos DB | 200GB storage, 2M ops | **$80-100** |
| Storage Account | 100GB | **$5** |
| Application Insights | 50GB logs | **$15** |
| **TOTAL** | | **$100-125/month** |

## 🎁 Free Tier Details

### What's Free Forever:
- **Azure Functions:** 1 million executions/month
- **Storage:** First 5GB
- **Application Insights:** First 5GB data/month
- **Cosmos DB:** Very light usage can be under $1

### What's Free for 12 Months (New Azure Accounts):
- $200 credit for first 30 days
- 12 months of free services
- After 12 months, you transition to pay-as-you-go

## 📊 Usage Examples

### Example 1: "Just Learning"
**Scenario:** Testing chatbot, asking 10 questions/day
- Requests: ~300/month
- Cost: **$0-1/month**

### Example 2: "Sharing with Friends"
**Scenario:** 10 friends using it, ~50 questions/day total
- Requests: ~1,500/month
- Cost: **$5-10/month**

### Example 3: "Small Community"
**Scenario:** 100 users, ~500 questions/day
- Requests: ~15,000/month
- Cost: **$20-30/month**

### Example 4: "Going Viral"
**Scenario:** Featured somewhere, 5,000 questions/day
- Requests: ~150,000/month
- Cost: **$50-70/month**

## 💡 Cost-Saving Tips

### 1. Use Free Tier Wisely
- Stay under 1M function calls/month = free functions
- Keep logs under 5GB = free monitoring
- Start small, scale gradually

### 2. Enable Auto-Shutdown
```bash
# Stop function app when not in use
az functionapp stop --name your-app --resource-group your-rg
```

### 3. Set Cosmos DB TTL
- Conversations auto-delete after 30 days
- Saves storage costs
- Already configured in terraform

### 4. Monitor Usage
```bash
# Check current costs
az consumption usage list --start-date 2026-01-01
```

### 5. Use Consumption Plan
- You're already using it (default in terraform)
- Only pay when functions run
- No charges when idle

## 🚨 Cost Alerts

### Set Up Billing Alert (Recommended!)

```bash
# Set alert at $10
az consumption budget create \
  --name "chatbot-budget" \
  --amount 10 \
  --time-grain Monthly \
  --start-date 2026-01-01 \
  --notifications \
    enabled=true \
    operator=GreaterThan \
    threshold=80 \
    contact-emails=your-email@example.com
```

### Azure Portal Method:
1. Go to portal.azure.com
2. Search "Cost Management"
3. Click "Budgets"
4. Create budget with alerts

## 📈 Scaling Costs

As your chatbot grows:

| Users/Day | Requests/Month | Est. Cost |
|-----------|----------------|-----------|
| 1-10 | 300-3,000 | $0-5 |
| 10-50 | 3K-15K | $10-20 |
| 50-200 | 15K-60K | $25-40 |
| 200-1K | 60K-300K | $50-80 |
| 1K-5K | 300K-1.5M | $100-150 |
| 5K+ | 1.5M+ | $200+ |

## 🔍 Real Cost Scenarios

### Scenario A: "Weekend Project"
**Reality:** Deployed Friday, tested over weekend, forgot about it
- Active: 2 days/month
- Cost: **$0-2/month**
- Risk: Low

### Scenario B: "Active Development"
**Reality:** Actively developing, testing daily for a month
- Active: 30 days/month, moderate testing
- Cost: **$5-15/month**
- Risk: Low

### Scenario C: "Shared with Community"
**Reality:** Posted link online, getting regular traffic
- Active: 24/7, organic traffic
- Cost: **$30-60/month**
- Risk: Medium (could spike)

### Scenario D: "Viral Post"
**Reality:** Featured somewhere popular, sudden traffic spike
- Active: High traffic for few days
- Cost: **$50-200/month**
- Risk: High (set budget alerts!)

## 🛡️ Protection Against Surprise Costs

### 1. Set Hard Limits in Code
```python
# Limit requests per user
MAX_REQUESTS_PER_DAY = 100
```

### 2. Set Azure Function Scale Limit
Already configured in terraform:
```hcl
app_scale_limit = 10  # Max 10 concurrent instances
```

### 3. Enable Budget Alerts
- $10 warning
- $25 alert
- $50 auto-stop (configure in Azure)

### 4. Monitor Daily
Check Azure Portal daily for first week after deployment.

## ❓ Common Questions

**Q: Can costs exceed $200/month unexpectedly?**
A: Unlikely with our configuration. Scale limit prevents runaway costs.

**Q: What if I forget to shut it down?**
A: With light usage, maybe $10-20/month. Set billing alert!

**Q: How do I stop all costs immediately?**
A: Run `terraform destroy` or delete resource group in Azure Portal.

**Q: Are there hidden fees?**
A: No. Azure pricing is transparent. Data transfer within Azure is free.

**Q: What's the cheapest way to learn?**
A: Use $200 free credit, set $10 alert, monitor daily. Should last 3+ months of learning.

## 📞 Need Help?

- **Azure Pricing Calculator:** https://azure.microsoft.com/pricing/calculator/
- **Cost Management:** Azure Portal → Cost Management + Billing
- **Support:** Azure Portal → Help + Support

## 🎯 Recommendation

**For Learning (First 3 Months):**
- Budget: $10-20/month
- Set alert at $10
- Check costs weekly
- Expected actual cost: $5-15/month

**For Production (After Validation):**
- Budget: $50-100/month
- Set alert at $50
- Check costs daily
- Expected actual cost: Depends on usage

---

**Remember:** Start small. Azure free tier is generous. You can learn for almost free, then scale when ready!