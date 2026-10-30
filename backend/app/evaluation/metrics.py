import numpy as np
from typing import List, Dict, Any

def compute_discounted_cumulative_gain(relevance_scores: List[float], k: int) -> float:
    """
    Computes DCG@K: sum_{i=1}^k (2^{rel_i} - 1) / log2(i + 1)
    """
    scores = relevance_scores[:k]
    dcg = 0.0
    for idx, rel in enumerate(scores):
        dcg += (2.0**rel - 1.0) / np.log2(idx + 2.0)
    return float(dcg)

def compute_ndcg_at_k(recommended_ids: List[str], ground_truth_relevance: Dict[str, float], k: int = 5) -> float:
    """
    Computes Normalized Discounted Cumulative Gain (NDCG@K).
    """
    actual_rels = [ground_truth_relevance.get(sid, 0.0) for sid in recommended_ids[:k]]
    actual_dcg = compute_discounted_cumulative_gain(actual_rels, k)

    # Ideal ranking DCG
    ideal_rels = sorted(ground_truth_relevance.values(), reverse=True)[:k]
    ideal_dcg = compute_discounted_cumulative_gain(ideal_rels, k)

    if ideal_dcg == 0:
        return 1.0 if actual_dcg == 0 else 0.0
    return float(round(actual_dcg / ideal_dcg, 3))

def compute_precision_at_k(recommended_ids: List[str], relevant_set: set, k: int = 5) -> float:
    """
    Precision@K = (# of relevant items in top K) / K
    """
    top_k = recommended_ids[:k]
    if not top_k:
        return 0.0
    hits = sum(1 for sid in top_k if sid in relevant_set)
    return float(round(hits / len(top_k), 3))

def compute_recall_at_k(recommended_ids: List[str], relevant_set: set, k: int = 5) -> float:
    """
    Recall@K = (# of relevant items in top K) / (total relevant items)
    """
    if not relevant_set:
        return 1.0
    top_k = recommended_ids[:k]
    hits = sum(1 for sid in top_k if sid in relevant_set)
    return float(round(hits / len(relevant_set), 3))

def compute_mean_reciprocal_rank(ranked_ids_list: List[List[str]], relevant_sets_list: List[set]) -> float:
    """
    MRR = (1 / |Q|) sum_{q=1}^{|Q|} (1 / rank_first_relevant)
    """
    rr_list = []
    for ranked_ids, rel_set in zip(ranked_ids_list, relevant_sets_list):
        reciprocal_rank = 0.0
        for idx, sid in enumerate(ranked_ids):
            if sid in rel_set:
                reciprocal_rank = 1.0 / (idx + 1)
                break
        rr_list.append(reciprocal_rank)

    return float(round(float(np.mean(rr_list)) if rr_list else 0.0, 3))
