class Bank {
    private long[] balance;
    private int n;

    public Bank(long[] balance) {
        this.balance = balance;
        this.n = balance.length;
    }

    public boolean isValidBankAccount(int account) {
        return account > 0 && account <= n;
    }

    public boolean hasEnoughBalance(long balance, long money) {
        return balance >= money;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if (isValidBankAccount(account1) && isValidBankAccount(account2)) {
            if (hasEnoughBalance(this.balance[account1 - 1], money)) {
                this.balance[account1 - 1] -= money;
                this.balance[account2 - 1] += money;
                return true;
            }
        }
        return false;
    }
    
    public boolean deposit(int account, long money) {
        if (isValidBankAccount(account)) {
            this.balance[account - 1] += money;
            return true;
        }
        return false;
    }
    
    public boolean withdraw(int account, long money) {
        if (isValidBankAccount(account)) {
            if (hasEnoughBalance(this.balance[account - 1], money)) {
                this.balance[account - 1] -= money;
                return true;
            }
        }
        return false;
    }
}