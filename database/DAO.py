from database.DB_connect import DBConnect
from model.album import Album


class DAO():
    @staticmethod
    def getAlbumsPerDurata(tempo):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select a.AlbumId, a.Title, a.ArtistId, (sum(t.Milliseconds))/1000/60 as Time
                    from track t, album a 
                    where t.AlbumId = a.AlbumId
                    group by t.AlbumId
                    having Time > %s
                    order by Time asc"""

        cursor.execute(query, (tempo,))
        result = []
        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct  t.albumId as a1, t2.AlbumId as a2
                    from track t, track t2, playlisttrack p1, playlisttrack p 
                    where t.TrackId = p1.TrackId
                    and t2.TrackId = p.TrackId
                    and p1.PlaylistId = p.PlaylistId 
                    and t.albumId <> t2.AlbumId """
        cursor.execute(query)
        result = []
        for row in cursor:
            if row["a1"] in idMap and row["a2"] in idMap:
                result.append((idMap[row["a1"]], idMap[row["a2"]]))
        return result
