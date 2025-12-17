# Обработчик командой строки
import argparse
import sys
from tabulate import tabulate

from .reader import ReadCsv
from .report import ReportOut


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Анализ эффективности работы разработчиков",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV файлам с данными разработчиков",
    )

    parser.add_argument(
        "--report",
        required=True,
        help=f"Название отчета. Доступные отчеты: {ReportOut.get_available_reports()}",
    )
    return parser.parse_args()


def main():
    try:
        args = parse_arguments()

        all_developers = []
        for filepath in args.files:
            print(f"Чтение файла: {filepath}")
            developers = ReadCsv.read_file(filepath)
            all_developers.extend(developers)
            print(f"  Прочитано записей: {len(developers)}")

        if not all_developers:
            print("\nОшибка: не найдено данных разработчиков", file=sys.stderr)
            sys.exit(1)

        print(f"\nВсего записей: {len(all_developers)}")

        # генерация отчета
        report = ReportOut.create_report(args.report)
        report_data = report.generate(all_developers)

        if not report_data:
            print("\nОтчет не содержит данных")
            return

        # отчет относительно эффективности
        if args.report == "performance":
            headers = ["position", "avg_performance", "count"]
            table_data = [
                [item["position"], item["avg_performance"], item["count"]]
                for item in report_data
            ]

        else:
            # Для других колонок
            headers = list(report_data[0].keys())
            table_data = [list(item.values()) for item in report_data]

        print(f"\nОтчет: {args.report}")
        print("=" * 50)
        print(tabulate(table_data, headers=headers, tablefmt="grid", floatfmt=".2f"))

    # вылавливание ошибок
    except FileNotFoundError as e:
        print(f"\nОшибка: {e}", file=sys.stderr)
        sys.exit(1)

    except ValueError as e:
        print(f"\nОшибка: {e}", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"\nНеожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
