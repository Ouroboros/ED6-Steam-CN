import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2104   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '戴尔蒙市长'),
    TXT(0x02, '尤莉亚中尉'),
    TXT(0x03, '亲卫队'),
    TXT(0x04, '亲卫队'),
    TXT(0x05, '亲卫队'),
    TXT(0x06, '亲卫队'),
    TXT(0x07, ' '),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2104.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA36
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
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
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH00005._CH', 'ED6_DT07/CH00005P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
        ('ED6_DT07/CH00045._CH', 'ED6_DT07/CH00045P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1BA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1BA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1C8',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    def _loc_1C8(): pass

    label('loc_1C8')

    Return()

# id: 0x0001 offset: 0x1C9
@scena.Code('Init')
def Init():
    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_72(0x0003, 0x0004)
    Event(0, 0x0002)
    PlaySE(452, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x1E1
@scena.Code('ReInit')
def ReInit():
    PlaySE(117, 0x00, 0x64)
    EventBegin(0x00)
    FadeIn(2000, 0)
    OP_B0(0x0002, 0x0F)
    CameraMove(-15160, -2990, -35260, 0)
    OP_67(0, 4070, -10000, 0)
    CameraSetDistance(1530, 0)
    OP_6C(0, 0)
    OP_6E(581, 0)
    OP_72(0x0001, 0x0002)
    OP_71(0x0001, 0x0040)
    OP_72(0x0000, 0x0002)
    OP_71(0x0000, 0x0040)
    OP_89(0x0101, 59410, -2000, -3710, 270)
    OP_89(0x0102, 61470, -2000, -4030, 270)
    OP_89(0x0105, 60400, -2000, -3500, 270)

    @scena.Lambda('lambda_027F')
    def lambda_027F():
        CameraMove(-14060, 2029, -15000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_027F)

    @scena.Lambda('lambda_0297')
    def lambda_0297():
        OP_6C(314000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0297)

    Sleep(3000)

    @scena.Lambda('lambda_02AC')
    def lambda_02AC():
        CameraSetDistance(2620, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_02AC)

    @scena.Lambda('lambda_02BC')
    def lambda_02BC():
        OP_67(0, 8750, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_02BC)

    OP_6E(904, 8000)
    TerminateThread(0x0101, 0xFF)
    Fade(1000)
    CameraMove(-6160, -2990, -12620, 0)
    OP_67(0, 4470, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    SetChrBattleFlags(0x0008, 0x0020)
    ClearChrFlags(0x0008, 0x0080)
    OP_89(0x0008, 1090, -2890, -16110, 270)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0490061773V#668F这、这飞艇是什么东西！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061774V是王国军的……\n',
            '不对，这个徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrBattleFlags(0x0009, 0x0020)
    SetChrBattleFlags(0x000A, 0x0020)
    SetChrBattleFlags(0x000B, 0x0020)
    SetChrBattleFlags(0x000C, 0x0020)
    SetChrBattleFlags(0x000D, 0x0020)
    OP_89(0x0009, -13380, 10050, -12580, 90)
    OP_89(0x000A, -15510, 10050, -11720, 90)
    OP_89(0x000B, -15520, 10050, -13390, 90)
    OP_89(0x000C, -15520, 10050, -13390, 90)
    OP_89(0x000D, -14360, 10050, -10980, 90)

    NpcTalk(
        0x0009,
        '女性的声音',
        (
            '#0100061775V#4P……王室亲卫队所属。\n',
            '高速巡洋舰『埃尔赛尤号』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061776V这就是本舰的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_047F')
    def lambda_047F():
        CameraMove(-6340, -540, -14100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_047F)

    @scena.Lambda('lambda_0497')
    def lambda_0497():
        OP_67(0, 5660, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0497)

    @scena.Lambda('lambda_04AF')
    def lambda_04AF():
        CameraSetDistance(2680, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_04AF)

    @scena.Lambda('lambda_04BF')
    def lambda_04BF():
        OP_6E(435, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_04BF)

    @scena.Lambda('lambda_04CF')
    def lambda_04CF():
        OP_6C(329000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_04CF)

    Sleep(3000)

    NpcTalk(
        0x0009,
        '女性军官',
        (
            '#0100061777V#170F咳咳……\n',
            '看来总算是赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061778V#668F蓝白色军服……\n',
            '难道是女王陛下的亲卫队！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '女性军官',
        (
            '#0100061779V#176F正是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061780V本人就是任职亲卫队中队长的\n',
            '尤莉亚·舒华兹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0100061781V#172F卢安市长，\n',
            '莫里斯·戴尔蒙先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061782V你涉嫌纵火、抢劫、强占等多项罪行，\n',
            '现在，我要将你拘捕归案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0490061783V#668F这是梦……\n',
            '一定是梦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061784V#664F啊……怎么搞的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, 370, -2300, -16090, 180)

    ExecExpressionWithValue(
        0x0008,
        0x2A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2C,
        (
            (Expr.PushLong, 0xFFFEA070),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrDirection(0x0008, 0, 300)
    PlaySE(524, 0x00, 0x64)
    OP_A1(0x000E, 0x0001)
    SetChrPos(0x000E, 25470, -2990, -32360, 114)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000E, 0x0004)
    SetChrFlags(0x0000, 0x0020)
    SetChrFlags(0x0001, 0x0020)
    SetChrFlags(0x0002, 0x0020)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 4)
    SetChrChipByIndex(0x0105, 5)

    @scena.Lambda('lambda_071D')
    def lambda_071D():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_071D)

    Sleep(1700)

    PlaySE(212, 0x00, 0x64)

    @scena.Lambda('lambda_0742')
    def lambda_0742():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0742)

    Sleep(700)

    @scena.Lambda('lambda_0762')
    def lambda_0762():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0762)

    Sleep(600)

    @scena.Lambda('lambda_0782')
    def lambda_0782():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0782)

    @scena.Lambda('lambda_079D')
    def lambda_079D():
        CameraMove(-10020, 100, -16530, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_079D)

    Sleep(400)

    @scena.Lambda('lambda_07BA')
    def lambda_07BA():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_07BA)

    Sleep(300)

    @scena.Lambda('lambda_07DA')
    def lambda_07DA():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_07DA)

    Sleep(200)

    @scena.Lambda('lambda_07FA')
    def lambda_07FA():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_07FA)

    Sleep(200)

    @scena.Lambda('lambda_081A')
    def lambda_081A():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_081A)

    Sleep(200)

    @scena.Lambda('lambda_083A')
    def lambda_083A():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_083A)

    Sleep(200)

    @scena.Lambda('lambda_085A')
    def lambda_085A():
        ChrMoveTo(0x00FE, -8430, -2990, -17280, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_085A)

    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0105, 65535)
    OP_0D()
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010061785V#004F这、这是……\n',
            '到底是怎么回事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061786V#014F我刚在想嘉恩先生请求支援的\n',
            '王国军能不能及时赶到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061787V即使是这样，\n',
            '军队也似乎来得太快了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061788V#048F……呵呵………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 135, 400)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0100061789V#171F啊，诸位游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100061790V很感谢诸位的帮忙。\n',
            '接下来的事就请交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    ClearMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2102._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
