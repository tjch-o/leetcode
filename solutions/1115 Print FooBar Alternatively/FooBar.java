import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

class FooBar {
    private int n;
    private ReentrantLock lock;
    private Condition cond;
    private boolean barTurn;

    public FooBar(int n) {
        this.n = n;
        this.lock = new ReentrantLock();
        this.cond = lock.newCondition();
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            try {
                lock.lock();

                while (barTurn) {
                    cond.await();
                }

                printFoo.run();
                barTurn = true;
                cond.signal();
            } finally {
                lock.unlock();
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            try {
                lock.lock();

                while (!barTurn) {
                    cond.await();
                }

                printBar.run();
                barTurn = false;
                cond.signal();
            } finally {
                lock.unlock();
            }
        }
    }
}