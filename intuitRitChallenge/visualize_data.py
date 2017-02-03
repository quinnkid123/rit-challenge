from intuitRitChallenge.models import Accounts, Transaction
import numpy as np
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import timeit

# def generate_table():
account_ids = []
vendor_ids = []
vendor_to_id = {}
i = 0

for user in Accounts.objects.all():
    for transaction in Transaction.objects.filter(owner=user):
        if transaction.vendor not in vendor_to_id:
            vendor_to_id[transaction.vendor] = len(vendor_to_id)
        account_ids.append(i)
        vendor_ids.append(vendor_to_id[transaction.vendor])
    i += 1

rows = np.array(account_ids)
cols = np.array(vendor_ids)
data = np.ones((len(account_ids),))
num_rows = len(vendor_to_id)
num_cols = i

adj = csr_matrix((data, (rows, cols)), shape=(num_rows, num_cols))
print(adj.shape)

# print("")
#
# accounts_per_vendor = adj.sum(axis=1).A1
# vendors = list(range(len(vendor_to_id)))
# for vendor in vendor_to_id:
#     vendors[vendor_to_id[vendor]] = vendor
#
# vendors = np.array(vendors)

X = adj

colors = 10*['r', 'g', 'b', 'c', 'k', 'y', 'm']
fig = plt.figure()
# plt.clf()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], X[i][2])

# ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], cluster_centers[:, 2],
#           marker="x", color='k', s=150, linewidths=5, zorder=10)

plt.show()


# if __name__ == "__main__":
#     print("Test")
#     start = timeit.default_timer()
#     table = generate_table()
#     print(table)
#     end = timeit.default_timer()
#     print("Took {}s to load".format(end - start))
