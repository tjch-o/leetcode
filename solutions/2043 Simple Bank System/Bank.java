class Bank {
    private long[] balance;

    public Bank(long[] balance) {
        this.balance = balance;
    }

    public boolean isValidAccount(int num) {
        return num >= 1 && num <= this.balance.length;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if (!isValidAccount(account1) || !isValidAccount(account2)) {
            return false;
        }

        if (this.balance[account1 - 1] < money) {
            return false;
        }
        this.balance[account1 - 1] -= money;
        this.balance[account2 - 1] += money;
        return true;
    }
    
    public boolean deposit(int account, long money) {
        if (!isValidAccount(account)) {
            return false;
        }
        
        this.balance[account - 1] += money;
        return true;
    }
    
    public boolean withdraw(int account, long money) {
        if (!isValidAccount(account) || this.balance[account - 1] < money) {
            return false;
        }

        this.balance[account - 1] -= money;
        return true;
    }
}