package exception;

@SuppressWarnings("serial")
public class InvalidNbOfCompetitorsException extends Exception {
	

	public InvalidNbOfCompetitorsException() {
		super();
	}

	public InvalidNbOfCompetitorsException(String message) {
		super(message);
	}

	public InvalidNbOfCompetitorsException(Throwable cause) {
		super(cause);
	}

	public InvalidNbOfCompetitorsException(String message, Throwable cause) {
		super(message, cause);
	}

	public InvalidNbOfCompetitorsException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
