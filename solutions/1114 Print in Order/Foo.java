import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

class Foo {
    private int step = 1;
    private ReentrantLock lock = new ReentrantLock();
    private Condition condition = lock.newCondition();

    public Foo() {}

    public void first(Runnable printFirst) throws InterruptedException {
        lock.lock();

        while (step != 1) {
            condition.await();
        }
        
        printFirst.run();
        step = 2;
        condition.signalAll();
        lock.unlock();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        lock.lock();

        while (step != 2) {
            condition.await();
        }
        
        printSecond.run();
        step = 3;
        condition.signalAll();
        lock.unlock();
    }

    public void third(Runnable printThird) throws InterruptedException {
        lock.lock();

        while (step != 3) {
            condition.await();
        }

        printThird.run();
        condition.signalAll();
        lock.unlock();
    }
}