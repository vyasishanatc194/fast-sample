from typing import List

from unidecode import unidecode

import utils
from CONSTANTS import CollInfo, DBInfo
from log import logger

from .mongo_connect import mongodb_client


async def get_club_id_name_photo_db(club_id: str):
    """Get club name and photo by club id.

    Args:
        club_id (str): club id.

    Returns:
        Dict[str, str]: club name and photo.
    """

    try:
        return mongodb_client[DBInfo.database][CollInfo.clubs].find_one(
            {"_id": club_id},
            {"name": 1, "photo_url": 1, "email": 1, "phone_number": 1},
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def get_club_name_photo_db(club_id: str):
    """Get club name and photo by club id.

    Args:
        club_id (str): club id.

    Returns:
        Dict[str, str]: club name and photo.
    """

    try:
        return mongodb_client[DBInfo.database][CollInfo.clubs].find_one(
            {"_id": club_id},
            {"_id": 0, "name": 1, "photo_url": 1, "email": 1, "timezone": 1},
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def get_club_full_info_from_db(id: str):
    """Fetches the club info from db

    Args:
        id (str):  Unique id of the club in mongodb generated by fb

    Returns:
        Dict: All info of club in the form of a dict
    """

    try:
        return mongodb_client[DBInfo.database][CollInfo.clubs].find_one({"_id": id})

    except Exception as e:
        utils.raise_exception(e=e)


async def get_club_name_currency_db(club_id: str):
    """Get club name and currency by club id.

    Args:
        club_id (str): club id.

    Returns:
        Dict[str, str]: club name and currency.
    """

    try:
        return mongodb_client[DBInfo.database][CollInfo.clubs].find_one(
            {"_id": club_id},
            {"_id": 0, "name": 1, "currency": 1},
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def generate_unique_short_name_with_name(name: str = "NONE") -> str:
    """Generate a short name from the given name.

    Args:
        name (str): Name

    Returns:
        str: Short name
    """

    try:
        club_docs = list(
            mongodb_client[DBInfo.database][CollInfo.clubs].find(
                {}, {"_id": 0, "short_name": 1}
            )
        )

        short_name_list: List[str] = [
            club.get("short_name") for club in club_docs if club.get("short_name")
        ]

        short_name = "".join(filter(str.isalnum, name))

        try:
            short_name = unidecode(short_name)
        except Exception as e:
            logger.error(f"Short name could not be unidecoded for {name}", e)

        short_name = short_name.replace(" ", "").strip().lower()

        if short_name in short_name_list:
            for i in range(len(short_name_list)):
                i += 1
                if short_name + str(i) not in short_name_list:
                    short_name = short_name + str(i)
                    break

    except Exception as e:
        utils.raise_exception(e=e)

    return short_name


async def get_club_full_info_with_shortname_from_db(club_short_name: str):
    """Fetches the club info from db

    Args:
        club_short_name (str):  Unique club_short_name of the club in mongodb

    Returns:
        Dict: All info of club in the form of a dict
    """

    try:
        return mongodb_client[DBInfo.database][CollInfo.clubs].find_one(
            {"short_name": club_short_name}
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def get_club_address_db(club_id: str):
    """Get club address by club id.

    Args:
        club_id (str): club id.

    Returns:
        Dict[str, str]: club address.
    """

    try:
        return mongodb_client[DBInfo.database][CollInfo.clubs].find_one(
            {"_id": club_id},
            {
                "_id": 1,
                "name": 1,
                "address": 1,
                "city": 1,
                "country": 1,
                "postal_code": 1,
            },
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def get_clubs_address_db(club_ids: List[str]):
    """Get club address by club ids.

    Args:
        club_ids (List[str]): club ids.

    Returns:
        Dict[str, str]: club address.
    """

    try:
        return list(
            mongodb_client[DBInfo.database][CollInfo.clubs].find(
                {"_id": {"$in": club_ids}, "removed": {"$ne": True}},
                {
                    "_id": 1,
                    "name": 1,
                    "address": 1,
                    "city": 1,
                    "country": 1,
                    "postal_code": 1,
                },
            )
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def get_clubs_names_db(club_ids: List[str]):
    """Get club names by club ids.

    Args:
        club_ids (List[str]): club ids.

    Returns:
        Dict[str, str]: club names.
    """

    try:
        return list(
            mongodb_client[DBInfo.database][CollInfo.clubs].find(
                {"_id": {"$in": club_ids}},
                {"_id": 1, "name": 1},
            )
        )
    except Exception as e:
        utils.raise_exception(e=e)


async def remove_club_db(club_id: str):
    """
    Removes a club from the MongoDB database.

    Parameters:
        club_id (str): The unique identifier of the club to be removed.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation in MongoDB.
    """

    try:
        # Update the document in the 'clubs' collection with the specified club_id,
        # marking it as removed by setting the 'removed' field to True.
        return mongodb_client[DBInfo.database][CollInfo.clubs].update_one(
            {
                "_id": club_id,
                "removed": {"$ne": True},
            },
            {"$set": {"removed": True}},
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def restore_club_db(club_id: str):
    """
    Restores a club in the MongoDB database.

    Parameters:
        club_id (str): The unique identifier of the club to be restored.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation in MongoDB.
    """

    try:
        # Update the document in the 'clubs' collection with the specified club_id,
        # marking it as restored by setting the 'removed' field to False.
        return mongodb_client[DBInfo.database][CollInfo.clubs].update_one(
            {
                "_id": club_id,
                "removed": {"$ne": False},
            },
            {"$set": {"removed": False}},
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def get_club_full_info_from_with_club_id_or_short_name_db(
    club_id_or_short_name: str,
):
    """Fetches the club info from db

    Args:
        club_id_or_short_name (str): Unique id of the club in mongodb generated by fb

    Returns:
        Dict: All info of club in the form of a dict
    """

    try:
        return mongodb_client[DBInfo.database][CollInfo.clubs].find_one(
            {
                "$or": [
                    {"_id": club_id_or_short_name},
                    {"short_name": club_id_or_short_name},
                ]
            }
        )

    except Exception as e:
        utils.raise_exception(e=e)


async def get_user_club_info_db(club_id: str):
    """Get club info for event logs.

    Args:
        club_id (str): club id.

    Returns:
        Dict[str, str]: club name and photo.
    """

    try:
        return mongodb_client[DBInfo.database][CollInfo.clubs].find_one(
            {"_id": club_id},
            {
                "_id": 0,
                "user_mongo_id": {"$literal": None},
                "user_firebase_id": "$_id",
                "user_email": "$email",
                "user_name": "$name",
                "user_photo": "$photo_url",
                "user_phone": "$phone_number",
            },
        )

    except Exception as e:
        utils.raise_exception(e=e)
