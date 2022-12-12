import unittest, os

if __name__ == '__main__':

    ttl_tests = 0
    ttl_error_tests = 0
    ttl_failed_tests = 0
    error_test_details = []
    failed_test_details = []

    # Run test1
    suite = unittest.TestLoader().discover(os.getcwd(), "test1" + ".py")
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)

    ttl_tests += results.testsRun
    ttl_error_tests += len(results.errors)
    ttl_failed_tests += len(results.failures)
    for error in results.errors:
        error_test_details.append(error)
    for failure in results.failures:
        failed_test_details.append(failure)

    # Run test2
    suite = unittest.TestLoader().discover(os.getcwd(), "test2" + ".py")
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)

    ttl_tests += results.testsRun
    ttl_error_tests += len(results.errors)
    ttl_failed_tests += len(results.failures)
    for error in results.errors:
        error_test_details.append(error)
    for failure in results.failures:
        failed_test_details.append(failure)

    with open(os.path.join(os.getcwd(), "log_test_suite_results.txt"), "w") as f:
        f.write("Num of tests: {}\n".format(ttl_tests))
        f.write("Num of passed tests: {}\n".format(ttl_tests - ttl_error_tests - ttl_failed_tests))
        f.write("Num of erroneous tests: {}\n".format(ttl_error_tests))
        f.write("Num of failed tests: {}\n\n".format(ttl_failed_tests))
        f.write("All Erroneous Tests:\n\n")
        for count, error in enumerate(error_test_details, 1):
            f.write("Erroneous Test Num '{}':\n".format(count, error))
            f.write("\tErroneous Test: {}\n".format(error[0]))
            f.write("\tError Details: {}\n\n".format(repr(error[1])))
        f.write("All Failed Tests:\n\n")
        for count, failure in enumerate(failed_test_details, 1):
            f.write("Failed Test Num '{}':\n".format(count))
            f.write("\tFailed Test: {}\n".format(failure[0]))
            f.write("\tFailure Details: {}\n\n".format(repr(failure[1])))

    print("Num of tests: {}\n".format(ttl_tests))
    print("Num of passed tests: {}\n".format(ttl_tests-ttl_error_tests-ttl_failed_tests))
    print("Num of erroneous tests: {}\n".format(ttl_error_tests))
    print("Num of failed tests: {}\n".format(ttl_failed_tests))
    print("\n\n")
    for count, error in enumerate(error_test_details, 1):
        print("Erroneous Test Num '{}':\n".format(count, error))
        print("\tErroneous Test: {}\n".format(error[0]))
        print("\tError Details: {}\n".format(repr(error[1])))
    print("\n\n")
    for count, failure in enumerate(failed_test_details, 1):
        print("Failed Test Num '{}':\n".format(count))
        print("\tFailed Test: {}\n".format(failure[0]))
        print("\tFailure Details: {}\n".format(repr(failure[1])))