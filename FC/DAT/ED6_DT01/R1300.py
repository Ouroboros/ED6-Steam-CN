import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1300.x'
    header.mapIndex       = 57
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFCD768,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFDA670,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 312,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 57,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT09/CH10370._CH', 'ED6_DT09/CH10370P._CP'),
        ('ED6_DT09/CH10371._CH', 'ED6_DT09/CH10371P._CP'),
        ('ED6_DT09/CH10360._CH', 'ED6_DT09/CH10360P._CP'),
        ('ED6_DT09/CH10361._CH', 'ED6_DT09/CH10361P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -209600,
            z                   = 20,
            y                   = -150000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -206360,
            z                   = 10,
            y                   = -150000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '东柏斯街道方向',
            x                   = -207930,
            z                   = -20,
            y                   = -167750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哈肯大门方向',
            x                   = -204120,
            z                   = -200,
            y                   = 1430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -218580,
            z           = -40,
            y           = -112680,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0107,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -226560,
            z           = -30,
            y           = -88140,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0108,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -200780,
            z           = -20,
            y           = -50350,
            word_0C     = 0x0000,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0108,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -194620,
            z           = -30,
            y           = -34740,
            word_0C     = 0x0000,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x010B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -211700,
            y           = -2000,
            z           = -151630,
            range       = -202854,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFDAA58,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10004 offset: 0x1E2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1E2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1F3',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    def _loc_1F3(): pass

    label('loc_1F3')

    Return()

# id: 0x0001 offset: 0x1F4
@scena.Code('func_01_1F4')
def func_01_1F4():
    OP_16(0x02, 4000, -336000, -210000, 196627)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_217',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)

    def _loc_217(): pass

    label('loc_217')

    Return()

# id: 0x0002 offset: 0x218
@scena.Code('func_02_218')
def func_02_218():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_22D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_218')

    def _loc_22D(): pass

    label('loc_22D')

    Return()

# id: 0x0003 offset: 0x22E
@scena.Code('func_03_22E')
def func_03_22E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '既然是市长的委托，那就没办法了。\n',
            '办事要快一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x26C
@scena.Code('func_04_26C')
def func_04_26C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哈肯门是与帝国接壤的国境。\n',
            '千万不要引起麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x2A8
@scena.Code('func_05_2A8')
def func_05_2A8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 4, 0x30C)),
            Expr.Return,
        ),
        'loc_2B2',
    )

    Jump('loc_C43')

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_7B4',
    )

    EventBegin(0x00)
    OP_4A(0x0008, 0)
    OP_4A(0x0009, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0101, 400)
    ChrTurnDirection(0x0009, 0x0101, 400)
    SetScenaFlags(ScenaFlag(0x0061, 4, 0x30C))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 6, 0x306)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BE',
    )

    ChrTalk(
        0x0008,
        (
            '#2470020683V站住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020684V前面是哈肯大门方向，\n',
            '现在禁止通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2480020685V任何无关人员一律禁止通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020686V#006F非常遗憾，我们就是相关人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45E')

    def _loc_3BE(): pass

    label('loc_3BE')

    ChrTalk(
        0x0008,
        (
            '#2470020687V哦，你们是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2480020688V我记得是游击士协会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020689V#006F嘿嘿，真遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020690V现在的我们是作为\n',
            '柏斯市长的使者来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45E(): pass

    label('loc_45E')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '出示了梅贝尔市长的信件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#2470020691V这个是，梅贝尔市长的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020692V#010F我们受市长的委托，\n',
            '来向摩尔根将军了解搜索情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020693V#020F顺便说一下，这是正式的委托书。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020694V如果不让我们通过的话，\n',
            '将来有什么后果恐怕你们担当不起哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020695V哎呀，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020696V没办法，让他们通过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2480020697V喂，这样好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#2470020698V说起梅贝尔市长，\n',
            '不就是柏斯地区的总负责人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020699V那可是不能小觑的人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2480020700V确实如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0000, 400)

    ChrTalk(
        0x0009,
        (
            '#2480020701V……喂，你们几个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0009,
        (
            '#2480020702V可以让你们通过，\n',
            '不过千万不要引起麻烦哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2480020703V现在可是非常时期，而且不管怎么说，\n',
            '那里毕竟是和帝国接壤的边境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020704V#006F好的好的，我们知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020705V#020F那么，我们过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    OP_4B(0x0008, 0)
    ChrSetDirection(0x0009, 180, 400)
    OP_4B(0x0009, 0)
    EventEnd(0x01)

    Jump('loc_C43')

    def _loc_7B4(): pass

    label('loc_7B4')

    EventBegin(0x00)

    @scena.Lambda('lambda_07BC')
    def lambda_07BC():
        CameraMove(-207880, 40, -151960, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_07BC)

    OP_4A(0x0008, 0)
    OP_4A(0x0009, 0)
    ChrTurnDirectionByPos(0x0000, -207880, -151960, 0)
    ChrTurnDirectionByPos(0x0001, -207880, -151960, 0)
    ChrTurnDirectionByPos(0x0002, -207880, -151960, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 6, 0x306)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BB4',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0000, 400)
    ChrTurnDirection(0x0009, 0x0000, 400)
    SetScenaFlags(ScenaFlag(0x0060, 6, 0x306))

    ChrTalk(
        0x0008,
        (
            '#2470020339V站住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020340V前面是哈肯大门方向，\n',
            '现在禁止通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2480020341V任何无关人员一律禁止通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020342V#009F什么呀，真小气～\n',
            '稍微看看又没什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2480020343V我说，这可不是闹着玩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020344V现在，国境师团正在集结军力\n',
            '搜索行踪不明的定期船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020345V麻烦你们不要妨碍我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020346V#020F我们根本没有妨碍你们的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020347V我们是游击士，\n',
            '即使这样也不能让我们通过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020348V游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020349V姑且不说你是不是……\n',
            '难道这两个少年也是游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020350V#502F嘿嘿，我们就是啊☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020351V#010F这是我们的游击士徽章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020352V这、这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020353V但是，就算是游击士也毫不例外，\n',
            '一律禁止通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2480020354V对对。\n',
            '你们马上离开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020355V#009F哼～\n',
            '真是不可理喻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020356V#010F没办法了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020357V我们还是先去柏斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C12')

    def _loc_BB4(): pass

    label('loc_BB4')

    ChrTurnDirection(0x0008, 0x0000, 400)
    ChrTurnDirection(0x0009, 0x0000, 400)

    ChrTalk(
        0x0009,
        (
            '#2480020358V我说了不行就是不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2470020359V想来的话过一阵子再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C12(): pass

    label('loc_C12')

    ChrMoveToRelative(0x0000, 0, 0, -2000, 3000, 0x00)
    ChrSetDirection(0x0008, 180, 0)
    OP_4B(0x0008, 0)
    ChrSetDirection(0x0009, 180, 0)
    OP_4B(0x0009, 0)
    Sleep(50)

    EventEnd(0x04)

    def _loc_C43(): pass

    label('loc_C43')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
